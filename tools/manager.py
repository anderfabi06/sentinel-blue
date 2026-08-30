from typing import Dict, Any, Callable

from tools.nmap_tool import run_nmap_scan
from tools.log_analyzer_tool import analyze_system_logs
from tools.whois_tool import run_whois # <----- IMPORTACION DE HERRAMIENTA

class ToolManager:
    """
    Gestor central de herramientas de Sentinel Blue.
    """

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register_tool(
        self,
        name: str,
        func: Callable
    ):
        self._tools[name] = func

    def execute_tool(
        self,
        name: str,
        **kwargs
    ) -> Any:

        if name not in self._tools:

            raise ValueError(
                f"La herramienta '{name}' "
                f"aún no ha sido registrada."
            )

        return self._tools[name](**kwargs)

    def get_available_tools(
        self
    ) -> Dict[str, Callable]:

        return self._tools


# ============================================================
# TOOL MANAGER GLOBAL
# ============================================================

tool_manager = ToolManager()


# ============================================================
# REGISTRO DE HERRAMIENTAS
# ============================================================

tool_manager.register_tool(
    "run_nmap_scan",
    run_nmap_scan
)

tool_manager.register_tool(
    "analyze_system_logs",
    analyze_system_logs
)
#MANERA EN COMO SE AGREGA LA HERRAMIENTA
tool_manager.register_tool(
    "run_whois" ,
    run_whois
)