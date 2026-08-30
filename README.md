🛡️ SENTINEL BLUE — AI-Powered NOC/SOC Assistant

🤖 Sentinel Blue es un agente de Inteligencia Artificial orientado a operaciones NOC/SOC. Permite analizar eventos y logs, utilizar herramientas de seguridad y asistir al operador en la detección, investigación y respuesta ante incidentes.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 ESTRUCTURA DEL PROYECTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

sentinel-blue/
│
├── 🤖 agent/                  → Agente IA + LangGraph
│   ├── graph.py
│   ├── prompts.py
│   └── state.py
│
├── ⚡ backend/                → API REST con FastAPI
│   └── app/
│       ├── api/
│       ├── core/
│       ├── db/
│       ├── schemas/
│       └── main.py
│
├── 🛠️ tools/                  → Herramientas utilizadas por el agente
│   ├── log_analyzer_tool.py
│   ├── manager.py
│   ├── nmap_tool.py
│   └── whois_tool.py
│
├── 🌐 frontend/               → Interfaz web
│
├── 🧪 labs_integrations/      → Integraciones desarrolladas por el equipo
│
├── 📚 docs/                   → Documentación del proyecto
│
├── 🧪 tests/                  → Pruebas
│
├── 💻 cli.py                  → Terminal interactiva
├── 📦 requirements.txt        → Dependencias de Python
├── 🐳 docker-compose.yml      → Configuración Docker
├── 🔐 .env                    → Variables de entorno (NO SUBIR)
└── 📖 README.md


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📥 INSTALACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔹 1. Descargar el repositorio

Clonar el proyecto desde GitHub:

git clone <URL_DEL_REPOSITORIO>

Entrar a la carpeta:

cd sentinel-blue

Comprobar que el repositorio está correctamente descargado:

git status


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐍 2. CREAR ENTORNO VIRTUAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El entorno virtual permite mantener las dependencias de Sentinel Blue separadas de las demás instalaciones de Python del equipo.

🐧 Linux / Debian / Ubuntu:

python3 -m venv venv

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▶️ 3. ACTIVAR ENTORNO VIRTUAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐧 Linux / Debian / Ubuntu:

source venv/bin/activate

✅ Si se activó correctamente aparecerá:

(venv)

Ejemplo:

(venv) usuario@pc:~/sentinel-blue$


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 4. INSTALAR DEPENDENCIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Con el entorno virtual ACTIVADO:

pip install -r requirements.txt

Opcionalmente actualizar pip:

python -m pip install --upgrade pip


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔐 5. CONFIGURAR VARIABLES DE ENTORNO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Crear un archivo:

.env

en la raíz del proyecto.

Ejemplo:

LLM_API_KEY=

DATABASE_URL=

WAZUH_URL=
WAZUH_USER=
WAZUH_PASSWORD=

ZABBIX_URL=
ZABBIX_TOKEN=

⚠️ IMPORTANTE:

🚫 NO subir el archivo .env a GitHub.

🔑 Las API Keys, contraseñas y tokens son privados.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💻 6. EJECUTAR SENTINEL BLUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Con el entorno virtual activado:

python cli.py

Esto iniciará la terminal interactiva del agente.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧪 8. EJECUTAR PRUEBAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

También existen pruebas individuales:

python test_api.py

python test_graph_mock.py


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛑 9. DESACTIVAR ENTORNO VIRTUAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cuando termines de trabajar:

deactivate

El indicador:

(venv)

desaparecerá de la terminal.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👥 DISTRIBUCIÓN DEL EQUIPO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👨‍💻 LÍDER
Responsabilidades:

🤖 Agente IA
🧠 LangGraph
⚡ Backend / FastAPI
🏗️ Arquitectura
🔌 Integración final

Carpetas principales:

agent/
backend/


👨‍💻 COMPAÑERO 1 — WAZUH

Responsable de:

🛡️ Wazuh
🚨 Security Monitoring
📄 Logs
🔔 Alertas

Carpeta:

labs_integrations/wazuh/


👨‍💻 COMPAÑERO 2 — ZABBIX

Responsable de:

📊 Zabbix
🖥️ Infrastructure Monitoring
📈 Métricas
🌐 Hosts
⚙️ Disponibilidad

Carpeta:

labs_integrations/zabbix/


👨‍💻 COMPAÑERO 3 — NETWORK / DECEPTION

Responsable de:

🍯 Cowrie
📡 TShark
🌐 Network Analysis

Carpeta:

labs_integrations/network_deception/


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧪 ¿DÓNDE DEBEN TRABAJAR LOS COMPAÑEROS?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cada integrante debe desarrollar inicialmente su integración dentro de:

labs_integrations/

Ejemplo:

🛡️ Wazuh:

labs_integrations/wazuh/

📊 Zabbix:

labs_integrations/zabbix/

🍯 Cowrie / TShark / Network:

labs_integrations/network_deception/


⚠️ IMPORTANTE:

Los compañeros NO deben modificar directamente:

agent/
backend/

para realizar sus primeras pruebas.

El flujo será:

🛠️ Herramienta
      ↓
🧪 Prueba individual
      ↓
📁 labs_integrations/
      ↓
✅ Validación
      ↓
📤 Pull Request
      ↓
👨‍💻 Revisión del Líder
      ↓
🔗 Integración
      ↓
🛡️ Sentinel Blue Core


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌿 GIT FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚫 NO hacer push directamente a main.

Cada integrante debe trabajar en su propia rama.


🔄 1. ACTUALIZAR MAIN

git checkout main

git pull origin main


🌱 2. CREAR UNA RAMA

git checkout -b feature/nombre-de-la-tarea

Ejemplos:

git checkout -b feature/wazuh-integration

git checkout -b feature/zabbix-integration

git checkout -b feature/cowrie-integration

git checkout -b feature/tshark-integration


💻 3. REALIZAR EL TRABAJO

Trabajar únicamente dentro de la rama creada.

Comprobar la rama actual:

git branch

La rama actual aparecerá con:

*

Ejemplo:

  main
* feature/wazuh-integration


🔍 4. REVISAR LOS CAMBIOS

git status


➕ 5. AGREGAR LOS CAMBIOS

git add .

También puedes agregar un archivo específico:

git add labs_integrations/wazuh/archivo.py


💾 6. CREAR COMMIT

git commit -m "feat: add wazuh integration"

Ejemplos:

git commit -m "feat: add zabbix integration"

git commit -m "feat: add cowrie integration"

git commit -m "fix: update log analyzer"

git commit -m "docs: update wazuh documentation"


☁️ 7. SUBIR LA RAMA

git push origin feature/wazuh-integration

La primera vez también puedes utilizar:

git push -u origin feature/wazuh-integration


🔀 8. CREAR PULL REQUEST

Después del push:

GitHub
  ↓
🔀 Pull Request
  ↓
👨‍💻 Revisión del Líder
  ↓
🧪 Validación
  ↓
✅ Aprobación
  ↓
🔗 Merge
  ↓
main


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 FLUJO DE TRABAJO DIARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cuando vuelvas a trabajar en el proyecto:

📁 Entrar al proyecto:

cd sentinel-blue

🐍 Activar entorno:

source venv/bin/activate

🔄 Actualizar:

git checkout main
git pull origin main

🌱 Crear rama:

git checkout -b feature/mi-tarea

💻 Trabajar:

Desarrollar → Probar → Corregir

📋 Revisar:

git status

➕ Agregar:

git add .

💾 Commit:

git commit -m "feat: descripcion"

☁️ Subir:

git push origin feature/mi-tarea

🔀 Pull Request en GitHub


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚫 ARCHIVOS QUE NO SE DEBEN SUBIR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nunca subir al repositorio:

🔐 .env
🐍 venv/
🐍 __pycache__/
🐍 *.pyc

El archivo .gitignore debe encargarse de ignorarlos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡️ REGLAS PRINCIPALES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ 🚫 Nunca hacer push directamente a main.

2️⃣ 🌱 Cada integrante trabaja en su propia rama.

3️⃣ 🧪 Probar los cambios antes de crear un Pull Request.

4️⃣ 📁 Las integraciones nuevas comienzan en labs_integrations/.

5️⃣ 🤝 No modificar agent/ ni backend/ sin coordinación con el Líder.

6️⃣ 🔐 Nunca subir credenciales, tokens o contraseñas.

7️⃣ 🔀 Todo cambio importante entra mediante Pull Request.

8️⃣ 👀 El Líder revisa los cambios antes del merge.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 SENTINEL BLUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 AI-Powered NOC/SOC Assistant

📡 MONITORIZAR
      ↓
🧠 ANALIZAR
      ↓
🚨 DETECTAR
      ↓
🔎 INVESTIGAR
      ↓
🛡️ RESPONDER
