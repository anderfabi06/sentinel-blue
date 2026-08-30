import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from langgraph.graph import StateGraph, END

from agent.state import AgentState
from agent.prompts import SYSTEM_PROMPT
from tools.manager import tool_manager


# ============================================================
# CONFIGURACIÓN
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY no está configurada.")

client = genai.Client(api_key=api_key)


# ============================================================
# HERRAMIENTAS
# ============================================================

tools_dict = tool_manager.get_available_tools()

gemini_tools = list(tools_dict.values())


# ============================================================
# EXTRAER FUNCTION CALLS
# ============================================================

def get_function_calls_from_response(response):
    """
    Obtiene las llamadas a herramientas realizadas por Gemini.

    Como el automatic function calling está desactivado,
    Gemini devuelve explícitamente las llamadas mediante
    response.function_calls.
    """

    if response is None:
        return []

    try:
        return response.function_calls or []

    except Exception:
        return []


# ============================================================
# NODO: GEMINI
# ============================================================

async def call_gemini(state: AgentState) -> AgentState:

    messages = state.get("messages", [])

    try:

        # ----------------------------------------------------
        # CONFIGURACIÓN DE GEMINI
        # ----------------------------------------------------

        config = types.GenerateContentConfig(

            system_instruction=SYSTEM_PROMPT,

            temperature=0.2,

            tools=gemini_tools,

            automatic_function_calling=(
                types.AutomaticFunctionCallingConfig(
                    disable=True
                )
            )
        )

        # ----------------------------------------------------
        # CONSULTAR GEMINI
        # ----------------------------------------------------

        response = client.models.generate_content(

            model="gemini-3.6-flash",

            contents=messages,

            config=config
        )

        # ----------------------------------------------------
        # GUARDAR RESPUESTA COMPLETA
        # ----------------------------------------------------

        state["last_response"] = response

        # ----------------------------------------------------
        # GUARDAR RESPUESTA EN HISTORIAL
        # ----------------------------------------------------

        if response.candidates:

            candidate_content = response.candidates[0].content

            if candidate_content:

                messages.append(candidate_content)

        # ----------------------------------------------------
        # DETECTAR FUNCTION CALLS
        # ----------------------------------------------------

        function_calls = get_function_calls_from_response(
            response
        )

        # ----------------------------------------------------
        # OBTENER RESPUESTA TEXTUAL
        # ----------------------------------------------------

        if function_calls:

            # Gemini está solicitando una herramienta.
            #
            # No intentamos utilizar response.text porque
            # la respuesta contiene un function_call.

            state["final_response"] = ""

        else:

            # Gemini terminó y devuelve una respuesta textual.

            try:

                text = response.text

            except Exception:

                text = None

            state["final_response"] = text or ""

    # --------------------------------------------------------
    # MANEJO DE ERRORES
    # --------------------------------------------------------

    except Exception as e:

        error_msg = str(e)

        if (
            "429" in error_msg
            or "RESOURCE_EXHAUSTED" in error_msg
        ):

            state["final_response"] = (
                "[!] Límite de velocidad alcanzado (429). "
                "Espera unos segundos e intenta nuevamente."
            )

        else:

            state["final_response"] = (
                "Error al procesar la solicitud con Gemini: "
                f"{error_msg}"
            )

    # --------------------------------------------------------
    # ACTUALIZAR ESTADO
    # --------------------------------------------------------

    state["messages"] = messages

    return state


# ============================================================
# NODO: EJECUTAR HERRAMIENTAS
# ============================================================

async def execute_tools_node(state: AgentState) -> AgentState:

    response = state.get("last_response")

    messages = state.get("messages", [])

    # --------------------------------------------------------
    # OBTENER FUNCTION CALLS
    # --------------------------------------------------------

    function_calls = get_function_calls_from_response(
        response
    )

    if not function_calls:

        return state

    response_parts = []

    # --------------------------------------------------------
    # EJECUTAR CADA HERRAMIENTA
    # --------------------------------------------------------

    for call in function_calls:

        tool_name = call.name

        tool_args = (
            dict(call.args)
            if call.args
            else {}
        )

        try:

            # ------------------------------------------------
            # EJECUCIÓN LOCAL
            # ------------------------------------------------

            tool_result = tool_manager.execute_tool(

                tool_name,

                **tool_args
            )

        except Exception as e:

            tool_result = {

                "status": "error",

                "message": (
                    f"Falla en ejecutor: {str(e)}"
                )
            }

        # ----------------------------------------------------
        # NORMALIZAR RESULTADO
        # ----------------------------------------------------

        if not isinstance(tool_result, dict):

            tool_result = {

                "result": tool_result
            }

        # ----------------------------------------------------
        # CREAR FUNCTION RESPONSE
        # ----------------------------------------------------

        response_parts.append(

            types.Part.from_function_response(

                name=tool_name,

                response=tool_result
            )
        )

    # --------------------------------------------------------
    # ENVIAR RESULTADOS A GEMINI
    # --------------------------------------------------------

    if response_parts:

        messages.append(

            types.Content(

                role="user",

                parts=response_parts
            )
        )

    # --------------------------------------------------------
    # ACTUALIZAR ESTADO
    # --------------------------------------------------------

    state["messages"] = messages

    return state


# ============================================================
# DECISIÓN DEL GRAFO
# ============================================================

def should_continue(state: AgentState) -> str:

    response = state.get("last_response")

    function_calls = get_function_calls_from_response(
        response
    )

    if function_calls:

        return "execute_tools"

    return END


# ============================================================
# CONSTRUCCIÓN DEL GRAFO
# ============================================================

workflow = StateGraph(AgentState)


# ------------------------------------------------------------
# NODO PRINCIPAL
# ------------------------------------------------------------

workflow.add_node(
    "agent",
    call_gemini
)


# ------------------------------------------------------------
# NODO DE HERRAMIENTAS
# ------------------------------------------------------------

workflow.add_node(
    "execute_tools",
    execute_tools_node
)


# ------------------------------------------------------------
# PUNTO DE ENTRADA
# ------------------------------------------------------------

workflow.set_entry_point(
    "agent"
)


# ------------------------------------------------------------
# DECISIÓN
# ------------------------------------------------------------

workflow.add_conditional_edges(

    "agent",

    should_continue
)


# ------------------------------------------------------------
# DESPUÉS DE EJECUTAR TOOL → GEMINI
# ------------------------------------------------------------

workflow.add_edge(

    "execute_tools",

    "agent"
)


# ============================================================
# COMPILAR AGENTE
# ============================================================

sentinel_agent = workflow.compile()
