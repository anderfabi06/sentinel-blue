#ELABORAMOS LA CREACION DE LA HERRAMIENTA 
import subprocess


def run_whois(target: str) -> dict:
    """
    Obtiene información WHOIS de un dominio o dirección IP.

    Args:
        target: Dominio o dirección IP a consultar.
    """

    try:
        result = subprocess.run(
            ["whois", target],
            capture_output=True,
            text=True,
            timeout=20
        )

        if result.returncode != 0:
            return {
                "status": "error",
                "target": target,
                "message": result.stderr.strip() or "WHOIS devolvió un error."
            }

        return {
            "status": "success",
            "target": target,
            "raw_output": result.stdout
        }

    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "target": target,
            "message": "Tiempo de espera agotado ejecutando WHOIS."
        }

    except Exception as e:
        return {
            "status": "error",
            "target": target,
            "message": str(e)
        }