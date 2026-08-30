import asyncio
import os
import sys

from dotenv import load_dotenv
from google.genai import types

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown


# ============================================================
# CONFIGURACIÓN
# ============================================================

load_dotenv()

console = Console()


# ============================================================
# CARGAR AGENTE
# ============================================================

try:
    from agent.graph import sentinel_agent

except ImportError as e:

    console.print(
        f"[bold red][FAIL][/bold red] Error de importación: {e}"
    )

    console.print(
        "       Ejecuta el script desde la raíz: "
        "[bright_black]python3 cli.py[/bright_black]"
    )

    sys.exit(1)


# ============================================================
# VALIDAR CONFIGURACIÓN
# ============================================================

if not os.getenv("GEMINI_API_KEY"):

    console.print(
        "[bold red][FAIL][/bold red] "
        "No se encontró GEMINI_API_KEY en las variables de entorno."
    )

    sys.exit(1)


# ============================================================
# HEADER
# ============================================================

def print_professional_header():

    header_content = (
        "[bold white]SENTINEL BLUE[/bold white] "
        "[bright_black]v1.0.0 │ SOC & NOC Autonomous Assistant[/bright_black]\n"
        "[bright_black]Engine:[/bright_black] "
        "[cyan]Gemini 3.6 Flash[/cyan]  "
        "[bright_black]│ Status:[/bright_black] "
        "[green]Active[/green]  "
        "[bright_black]│ Tools:[/bright_black] "
        "[cyan]Loaded[/cyan]\n"
        "[bright_black]Commands:[/bright_black] "
        "[white]clear[/white] "
        "[bright_black]•[/bright_black] "
        "[white]reset[/white] "
        "[bright_black]•[/bright_black] "
        "[white]exit[/white]"
    )

    console.print(
        Panel(
            header_content,
            border_style="blue",
            expand=False
        )
    )


# ============================================================
# EXTRAER RESPUESTA TEXTUAL
# ============================================================

def extract_text_from_history(messages):

    if not messages:
        return ""

    last_msg = messages[-1]

    if not hasattr(last_msg, "parts"):
        return ""

    if not last_msg.parts:
        return ""

    text_parts = []

    for part in last_msg.parts:

        if hasattr(part, "text") and part.text:

            text_parts.append(part.text)

    return "\n".join(text_parts)


# ============================================================
# MAIN
# ============================================================

async def main():

    # Limpiar terminal
    os.system(
        "clear"
        if os.name == "posix"
        else "cls"
    )

    # Mostrar interfaz
    print_professional_header()

    # Historial de conversación
    messages_history = []

    while True:

        try:

            # ====================================================
            # INPUT DEL ANALISTA
            # ====================================================

            prompt_text = (
                "[bold cyan]sentinel-blue[/bold cyan]"
                "[bright_black]#[/bright_black] "
            )

            user_input = console.input(
                prompt_text
            ).strip()


            # ====================================================
            # IGNORAR INPUT VACÍO
            # ====================================================

            if not user_input:
                continue


            # ====================================================
            # COMANDOS
            # ====================================================

            if user_input.lower() in [
                "salir",
                "exit",
                "quit",
                "q"
            ]:

                console.print(
                    "\n[bright_black]"
                    "[INFO] Cerrando sesión y liberando recursos..."
                    "[/bright_black]\n"
                )

                break


            if user_input.lower() == "clear":

                os.system(
                    "clear"
                    if os.name == "posix"
                    else "cls"
                )

                print_professional_header()

                continue


            if user_input.lower() == "reset":

                messages_history.clear()

                console.print(
                    "\n[bright_black]"
                    "[INFO] Contexto de conversación reiniciado."
                    "[/bright_black]\n"
                )

                continue


            # ====================================================
            # MENSAJE DEL USUARIO
            # ====================================================

            messages_history.append(
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(
                            text=user_input
                        )
                    ]
                )
            )


            # ====================================================
            # ESTADO DEL AGENTE
            # ====================================================

            state_input = {

                "messages": messages_history,

                "last_response": None,

                "final_response": ""

            }


            # ====================================================
            # EJECUTAR LANGGRAPH
            # ====================================================

            with console.status(
                "[bright_black]"
                "[•] Evaluando heurística y herramientas..."
                "[/bright_black]",
                spinner="dots"
            ):

                final_state = await sentinel_agent.ainvoke(
                    state_input
                )


            # ====================================================
            # ACTUALIZAR HISTORIAL
            # ====================================================

            messages_history = final_state.get(
                "messages",
                messages_history
            )


            # ====================================================
            # OBTENER RESPUESTA FINAL
            # ====================================================

            bot_response = final_state.get(
                "final_response",
                ""
            )


            # ====================================================
            # RESPALDO: BUSCAR TEXTO EN HISTORIAL
            # ====================================================

            if not bot_response:

                bot_response = extract_text_from_history(
                    messages_history
                )


            # ====================================================
            # SIN RESPUESTA
            # ====================================================

            if not bot_response:

                bot_response = (
                    "*Sin respuesta procesable "
                    "emitida por la entidad.*"
                )


            # ====================================================
            # MOSTRAR RESPUESTA
            # ====================================================

            console.print(
                "\n[bold blue]─► Sentinel Blue[/bold blue]"
            )

            console.print(
                Markdown(bot_response)
            )

            console.print()


        # ========================================================
        # CTRL + C
        # ========================================================

        except KeyboardInterrupt:

            console.print(
                "\n\n[bright_black]"
                "[INFO] Interrupción por señal SIGINT. "
                "Saliendo..."
                "[/bright_black]\n"
            )

            break


        # ========================================================
        # ERROR GENERAL
        # ========================================================

        except Exception as e:

            console.print(
                f"\n[bold red][ERROR][/bold red] "
                f"{str(e)}\n"
            )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    asyncio.run(main())

