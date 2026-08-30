from typing import TypedDict, List, Any


class AgentState(TypedDict, total=False):
    """
    Estado principal de Sentinel Blue.

    Mantiene la información necesaria durante
    el ciclo de LangGraph:
    
    Usuario
        ↓
    Gemini
        ↓
    Function Call
        ↓
    Herramienta
        ↓
    Resultado
        ↓
    Gemini
        ↓
    Respuesta final
    """

    # Historial de conversación y mensajes
    messages: List[Any]

    # Última respuesta completa generada por Gemini
    last_response: Any

    # Respuesta final que será mostrada en el CLI
    final_response: str