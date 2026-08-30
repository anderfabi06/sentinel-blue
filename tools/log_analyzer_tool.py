# tools/log_analyzer_tool.py
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

def analyze_system_logs(log_type: str = "auth", lines: int = 50) -> dict:
    """
    Analiza y extrae los últimos eventos de los logs del sistema Linux.
    
    Args:
        log_type: El tipo de log a analizar ('auth' para accesos/SSH, 'syslog' para eventos generales, 'dmesg' para kernel).
        lines: Número de líneas recientes a inspeccionar (por defecto 50).
    """
    try:
        if log_type == "auth":
            log_path = "/var/log/auth.log"
        elif log_type == "syslog":
            log_path = "/var/log/syslog"
        else:
            return {"status": "error", "message": f"Tipo de log '{log_type}' no soportado."}

        # Si el archivo no existe o requiere permisos, intentamos leer vía journalctl o tail
        if os.path.exists(log_path):
            cmd = ["tail", "-n", str(lines), log_path]
        else:
            # Alternativa para sistemas con systemd / journalctl
            unit = "ssh" if log_type == "auth" else "systemd"
            cmd = ["journalctl", "-u", unit, "-n", str(lines), "--no-pager"]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        logs = result.stdout.strip()

        if not logs:
            return {"status": "success", "message": "No se encontraron entradas recientes en los logs."}

        return {
            "status": "success",
            "log_type": log_type,
            "lines_analyzed": lines,
            "raw_logs": logs
        }

    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": f"Error ejecutando comando de logs: {e.stderr}"}
    except Exception as e:
        return {"status": "error", "message": f"Falla al leer logs: {str(e)}"}