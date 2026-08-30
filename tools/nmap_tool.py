import subprocess


def run_nmap_scan(target_ip: str) -> dict:
    """
    Ejecuta un escaneo rápido de puertos y servicios
    contra una IP o hostname autorizado.

    Args:
        target_ip:
            IP o hostname objetivo.

    Returns:
        Diccionario con el resultado del escaneo.
    """

    try:

        cmd = [
            "nmap",
            "-Pn",
            "-F",
            "-sV",
            "-n",
            "--host-timeout",
            "30s",
            target_ip
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=35
        )

        if result.returncode == 0:

            return {
                "status": "success",
                "target": target_ip,
                "raw_output": result.stdout
            }

        return {
            "status": "error",
            "target": target_ip,
            "message": (
                result.stderr
                or "Error desconocido al ejecutar Nmap."
            )
        }

    except subprocess.TimeoutExpired:

        return {
            "status": "error",
            "target": target_ip,
            "message": (
                "Tiempo de espera agotado "
                "al ejecutar Nmap."
            )
        }

    except Exception as e:

        return {
            "status": "error",
            "target": target_ip,
            "message": str(e)
        }