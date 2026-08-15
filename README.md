# 🛡️ SENTINEL BLUE — AI-Powered NOC/SOC Assistant

Plataforma inteligente de ciberseguridad defensiva y respuesta guiada asistida por IA para equipos NOC/SOC.

## 📁 Estructura del Repositorio

- `backend/`: API REST en FastAPI (Desarrollo del Líder).
- `agent/`: Orquestación del Agente de IA con LangGraph y DeepSeek (Desarrollo del Líder).
- `tools/`: Módulo unificado de herramientas consumidas por el Agente.
- `frontend/`: Interfaz Web (HTML5, JS, Bootstrap, Chart.js).
- `labs_integrations/`: **Espacio asignado para las pruebas y scripts del equipo.**
  - `/wazuh`: Compañero 1
  - `/zabbix`: Compañero 2
  - `/network_deception`: Compañero 3 (Cowrie, Nmap, TShark)

## 🚀 Reglas de Trabajo (Git Flow)

1. Nadie hace `push` directo a la rama `main`.
2. Cada integrante crea su rama: `git checkout -b feature/nombre-tarea`.
3. Para entregar un avance, sube tu rama y abre un **Pull Request** en GitHub para revisión del Líder.
