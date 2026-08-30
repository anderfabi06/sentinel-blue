import asyncio
from unittest.mock import MagicMock, patch

from google.genai import types

from agent.graph import sentinel_agent


# ============================================================
# CONFIGURACIÓN DE PRUEBAS
# ============================================================

TESTS = [
    {
        "name": "NMAP",
        "tool_name": "run_nmap_scan",
        "tool_args": {
            "target_ip": "127.0.0.1"
        },
        "user_message": "Ejecuta un Nmap contra 127.0.0.1"
    },
    {
        "name": "LOG ANALYZER",
        "tool_name": "analyze_system_logs",
        "tool_args": {
            "log_type": "auth",
            "lines": 20
        },
        "user_message": "Analiza los últimos 20 eventos de autenticación SSH"
    },
    {
        "name": "WHOIS",
        "tool_name": "run_whois",
        "tool_args": {
            "target": "example.com"
        },
        "user_message": "Realiza un WHOIS de example.com"
    }
]


# ============================================================
# CREAR RESPUESTAS MOCK DE GEMINI
# ============================================================

def build_mock_responses(tool_name, tool_args):
    """
    Simula las dos respuestas que Gemini produciría:

    Fase 1:
        Gemini solicita ejecutar una herramienta.

    Fase 2:
        Gemini recibe el resultado y genera una respuesta final.
    """

    # ========================================================
    # FASE 1 - FUNCTION CALL
    # ========================================================

    part_call = types.Part.from_function_call(
        name=tool_name,
        args=tool_args
    )

    content_call = types.Content(
        role="model",
        parts=[part_call]
    )

    candidate_call = MagicMock()
    candidate_call.content = content_call

    mock_resp_call = MagicMock()

    mock_resp_call.candidates = [
        candidate_call
    ]

    mock_resp_call.function_calls = [
        part_call.function_call
    ]

    mock_resp_call.text = None


    # ========================================================
    # FASE 2 - RESPUESTA FINAL
    # ========================================================

    part_text = types.Part.from_text(
        text=(
            f"[MOCK SENTINEL BLUE] "
            f"La herramienta '{tool_name}' "
            f"fue ejecutada correctamente. "
            f"Resultado procesado por el agente."
        )
    )

    content_final = types.Content(
        role="model",
        parts=[part_text]
    )

    candidate_final = MagicMock()
    candidate_final.content = content_final

    mock_resp_final = MagicMock()

    mock_resp_final.candidates = [
        candidate_final
    ]

    mock_resp_final.function_calls = []

    mock_resp_final.text = part_text.text


    return mock_resp_call, mock_resp_final


# ============================================================
# EJECUTAR UNA PRUEBA
# ============================================================

async def run_tool_test(test):

    tool_name = test["tool_name"]
    tool_args = test["tool_args"]
    user_message = test["user_message"]

    print("\n")
    print("=" * 65)
    print(f" TEST: {test['name']}")
    print("=" * 65)

    print(f"[*] Herramienta : {tool_name}")
    print(f"[*] Argumentos   : {tool_args}")
    print(f"[*] Usuario      : {user_message}")


    # ========================================================
    # CREAR RESPUESTAS MOCK
    # ========================================================

    mock_resp_call, mock_resp_final = build_mock_responses(
        tool_name,
        tool_args
    )


    # ========================================================
    # REEMPLAZAR GEMINI POR MOCK
    # ========================================================

    with patch(
        "agent.graph.client.models.generate_content"
    ) as mock_generate:

        mock_generate.side_effect = [
            mock_resp_call,
            mock_resp_final
        ]


        # ====================================================
        # ESTADO INICIAL
        # ====================================================

        initial_input = {

            "messages": [

                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(
                            text=user_message
                        )
                    ]
                )

            ],

            "last_response": None,

            "final_response": ""
        }


        # ====================================================
        # EJECUTAR LANGGRAPH
        # ====================================================

        final_state = await sentinel_agent.ainvoke(
            initial_input
        )


    # ========================================================
    # ANALIZAR RESULTADO
    # ========================================================

    messages = final_state.get(
        "messages",
        []
    )

    tool_executed = False

    tool_result = None


    for msg in messages:

        if not hasattr(msg, "parts"):
            continue

        if not msg.parts:
            continue

        for part in msg.parts:

            if (
                hasattr(part, "function_response")
                and part.function_response
            ):

                tool_executed = True

                tool_result = (
                    part.function_response.response
                )

                print(
                    f"\n[+] Herramienta detectada: "
                    f"{part.function_response.name}"
                )

                print(
                    "[+] Resultado local obtenido:"
                )

                print(
                    f"    Status: "
                    f"{tool_result.get('status')}"
                )

                # ====================================================
                # MOSTRAR INFORMACIÓN RELEVANTE
                # ====================================================

                if "target" in tool_result:

                    print(
                        f"    Target: "
                        f"{tool_result.get('target')}"
                    )

                if "log_type" in tool_result:

                    print(
                        f"    Log type: "
                        f"{tool_result.get('log_type')}"
                    )

                if "lines_analyzed" in tool_result:

                    print(
                        f"    Lines: "
                        f"{tool_result.get('lines_analyzed')}"
                    )

                if "raw_output" in tool_result:

                    raw_output = tool_result.get(
                        "raw_output",
                        ""
                    )

                    print(
                        "    Output:"
                    )

                    for line in raw_output.splitlines()[:5]:

                        print(
                            f"      {line}"
                        )

                if "raw_logs" in tool_result:

                    raw_logs = tool_result.get(
                        "raw_logs",
                        ""
                    )

                    print(
                        "    Logs:"
                    )

                    for line in raw_logs.splitlines()[:5]:

                        print(
                            f"      {line}"
                        )

                if "message" in tool_result:

                    print(
                        f"    Message: "
                        f"{tool_result.get('message')}"
                    )


    # ========================================================
    # RESULTADO
    # ========================================================

    if tool_executed:

        print(
            f"\n[✓] PASS: "
            f"'{tool_name}' fue ejecutada "
            f"y procesada por LangGraph."
        )

    else:

        print(
            f"\n[✗] FAIL: "
            f"No se detectó la ejecución de "
            f"'{tool_name}'."
        )


    print(
        "\n[+] Respuesta final:"
    )

    print(
        final_state.get(
            "final_response",
            "[SIN RESPUESTA]"
        )
    )

    print("=" * 65)

    return tool_executed


# ============================================================
# SUITE COMPLETA
# ============================================================

async def main():

    print("=" * 65)

    print(
        "  SENTINEL BLUE - TOOL TEST SUITE"
    )

    print(
        "  MOCK GEMINI │ 0 TOKENS"
    )

    print("=" * 65)


    results = []


    for test in TESTS:

        try:

            success = await run_tool_test(
                test
            )

            results.append(
                (
                    test["name"],
                    success
                )
            )

        except Exception as e:

            print(
                f"\n[✗] ERROR EN TEST "
                f"{test['name']}: {e}"
            )

            results.append(
                (
                    test["name"],
                    False
                )
            )


    # ========================================================
    # RESUMEN
    # ========================================================

    print("\n")
    print("=" * 65)
    print("  RESUMEN DE PRUEBAS")
    print("=" * 65)


    passed = 0


    for name, success in results:

        if success:

            print(
                f"[✓] PASS  {name}"
            )

            passed += 1

        else:

            print(
                f"[✗] FAIL  {name}"
            )


    print("-" * 65)

    print(
        f"Resultado: "
        f"{passed}/{len(results)} pruebas exitosas"
    )

    print("=" * 65)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    asyncio.run(main())
