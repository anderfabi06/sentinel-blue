Sí, ya veo el problema de tu README actual: **GitHub está interpretando parte de la estructura como texto corrido**, por eso se ve amontonado. Hay que separar bien los títulos, usar bloques de código para comandos y estructura, y tablas para distribución.

Te recomiendo este README. Está hecho específicamente para **tu estructura actual y para que tus compañeros sepan exactamente cómo descargar, ejecutar y trabajar con Git**.

````markdown
# 🛡️ Sentinel Blue

### AI-Powered NOC/SOC Assistant

Sentinel Blue es un agente de Inteligencia Artificial orientado a operaciones **NOC/SOC**, diseñado para analizar eventos y logs, utilizar herramientas de seguridad y asistir al operador en la detección, investigación y respuesta ante incidentes.

> 🚧 **Estado:** En desarrollo

---

## 📌 ¿Qué es Sentinel Blue?

Sentinel Blue busca centralizar diferentes herramientas de monitoreo y seguridad dentro de un agente inteligente.

El proyecto combina:

- 🤖 Inteligencia Artificial
- 🧠 LangGraph
- ⚡ FastAPI
- 🛠️ Herramientas de seguridad
- 📊 Monitorización
- 🔎 Análisis de logs
- 🌐 Network Analysis
- 🐳 Docker
- 🗄️ Base de datos

La arquitectura está diseñada para que cada integrante del equipo pueda desarrollar una herramienta o integración de manera independiente y posteriormente incorporarla al núcleo de Sentinel Blue.

---

# 📁 Estructura del proyecto

```text
sentinel-blue/
│
├── 🤖 agent/
│   ├── graph.py
│   ├── prompts.py
│   └── state.py
│
├── ⚡ backend/
│   └── app/
│       ├── api/
│       ├── core/
│       ├── db/
│       ├── schemas/
│       └── main.py
│
├── 📚 docs/
│
├── 🌐 frontend/
│
├── 🧪 labs_integrations/
│
├── 🛠️ tools/
│   ├── log_analyzer_tool.py
│   ├── manager.py
│   ├── nmap_tool.py
│   └── whois_tool.py
│
├── 🧪 tests/
│
├── 💻 cli.py
├── 🐳 docker-compose.yml
├── 📦 requirements.txt
├── 🔐 .env
├── 🚫 .gitignore
├── 🧪 test_api.py
├── 🧪 test_graph_mock.py
└── 📖 README.md
````

---

# 🧩 Descripción de las carpetas

## 🤖 `agent/`

Contiene el núcleo del **Agente de IA**.

```text
agent/
├── graph.py
├── prompts.py
└── state.py
```

* `graph.py` → flujo de ejecución del agente mediante LangGraph.
* `prompts.py` → prompts e instrucciones del agente.
* `state.py` → estado utilizado durante la ejecución.

> ⚠️ Esta carpeta forma parte del núcleo del proyecto. No modificarla sin coordinación con el Líder.

---

## ⚡ `backend/`

Contiene el backend desarrollado con **FastAPI**.

```text
backend/
└── app/
    ├── api/
    ├── core/
    ├── db/
    ├── schemas/
    └── main.py
```

* `api/` → endpoints de la API.
* `core/` → configuraciones y componentes centrales.
* `db/` → conexión y lógica de base de datos.
* `schemas/` → modelos para validar datos.
* `main.py` → punto de entrada de FastAPI.

> ⚠️ El backend forma parte del núcleo de Sentinel Blue. Los integrantes encargados de herramientas no deben modificarlo directamente sin coordinación.

---

## 🛠️ `tools/`

Contiene las herramientas que puede utilizar el agente.

```text
tools/
├── log_analyzer_tool.py
├── manager.py
├── nmap_tool.py
└── whois_tool.py
```

### 🔎 Nmap

`nmap_tool.py`

Permite realizar tareas de reconocimiento autorizadas.

### 🌐 WHOIS

`whois_tool.py`

Permite realizar consultas WHOIS.

### 📄 Log Analyzer

`log_analyzer_tool.py`

Permite analizar logs y obtener información relevante.

### 🧰 Tool Manager

`manager.py`

Gestiona las herramientas disponibles para el agente.

---

## 🌐 `frontend/`

Contiene la interfaz web de Sentinel Blue.

Aquí se desarrollará el Dashboard y la interfaz para interactuar con el agente.

---

## 🧪 `labs_integrations/`

Esta es la zona principal de trabajo para los integrantes encargados de las herramientas externas.

Aquí se desarrollan y prueban las integraciones antes de conectarlas al núcleo de Sentinel Blue.

```text
labs_integrations/
│
├── wazuh/
├── zabbix/
└── network_deception/
```

---

# 👥 Distribución del equipo

| Integrante      | Responsabilidad                       | Carpeta                                |
| --------------- | ------------------------------------- | -------------------------------------- |
| 👨‍💻 Líder     | IA, LangGraph, Backend y arquitectura | `agent/` `backend/`                    |
| 🛡️ Compañero 1 | Wazuh                                 | `labs_integrations/wazuh/`             |
| 📊 Compañero 2  | Zabbix                                | `labs_integrations/zabbix/`            |
| 🌐 Compañero 3  | Cowrie, TShark y Network              | `labs_integrations/network_deception/` |

---

# 🚀 Instalación

## 1. 📥 Descargar el repositorio

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Entrar al proyecto:

```bash
cd sentinel-blue
```

Comprobar que el repositorio funciona correctamente:

```bash
git status
```

---

## 2. 🐍 Crear entorno virtual

Cada integrante debe utilizar su propio entorno virtual.

### 🐧 Linux / Debian / Ubuntu

```bash
python3 -m venv venv
```

### 🪟 Windows

```bash
python -m venv venv
```

---

## 3. ▶️ Activar el entorno virtual

### 🐧 Linux / Debian / Ubuntu

```bash
source venv/bin/activate
```

### 🪟 Windows CMD

```cmd
venv\Scripts\activate
```

### 🪟 Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

Si se activó correctamente aparecerá:

```text
(venv)
```

al inicio de la terminal.

Ejemplo:

```text
(venv) usuario@pc:~/sentinel-blue$
```

---

## 4. 📦 Instalar dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Opcionalmente actualizar `pip`:

```bash
python -m pip install --upgrade pip
```

---

# 🔐 Configuración del `.env`

Sentinel Blue utiliza variables de entorno para almacenar configuraciones y credenciales.

Crear un archivo:

```text
.env
```

en la raíz del proyecto.

Ejemplo:

```env
LLM_API_KEY=

DATABASE_URL=

WAZUH_URL=
WAZUH_USER=
WAZUH_PASSWORD=

ZABBIX_URL=
ZABBIX_TOKEN=
```

⚠️ **Nunca subir el `.env` a GitHub.**

Cada integrante debe utilizar sus propias credenciales.

Se recomienda mantener un archivo:

```text
.env.example
```

con las variables vacías para que todos sepan qué configuración necesitan.

---

# 💻 Ejecutar Sentinel Blue

Una vez activado el entorno virtual:

```bash
python cli.py
```

Esto iniciará la terminal interactiva de Sentinel Blue.

Ejemplo:

```text
╔══════════════════════════════════════╗
║          🛡️ SENTINEL BLUE            ║
║       🤖 AI NOC/SOC ASSISTANT        ║
╚══════════════════════════════════════╝

Sentinel Blue >
```

---

# ⚡ Ejecutar el Backend

Activar primero el entorno virtual.

Después:

```bash
uvicorn backend.app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Ejecutar pruebas

Ejecutar las pruebas:

```bash
pytest
```

También se pueden ejecutar individualmente:

```bash
python test_api.py
```

```bash
python test_graph_mock.py
```

---

# 🛑 Desactivar el entorno virtual

Cuando termines de trabajar:

```bash
deactivate
```

El indicador:

```text
(venv)
```

desaparecerá de la terminal.

---

# 🔀 Flujo de trabajo del equipo

Cada integrante debe seguir este flujo:

```text
📥 Descargar repositorio
        ↓
🐍 Crear entorno virtual
        ↓
📦 Instalar dependencias
        ↓
🔐 Configurar .env
        ↓
🔄 Actualizar main
        ↓
🌱 Crear rama
        ↓
💻 Desarrollar
        ↓
🧪 Probar
        ↓
💾 Commit
        ↓
☁️ Push
        ↓
🔀 Pull Request
        ↓
👨‍💻 Revisión
        ↓
✅ Merge
```

---

# 🌿 Git Flow

## 🚫 Regla principal

**NO hacer `push` directamente a `main`.**

La rama `main` debe mantenerse estable.

Cada integrante debe trabajar en su propia rama.

---

## 1. 🔄 Actualizar `main`

Antes de comenzar una nueva tarea:

```bash
git checkout main
```

```bash
git pull origin main
```

---

## 2. 🌱 Crear una rama

Crear una rama específica para la tarea:

```bash
git checkout -b feature/nombre-de-la-tarea
```

Ejemplos:

```bash
git checkout -b feature/wazuh-integration
```

```bash
git checkout -b feature/zabbix-integration
```

```bash
git checkout -b feature/cowrie-integration
```

```bash
git checkout -b feature/tshark-integration
```

---

## 3. 💻 Realizar el trabajo

Trabajar dentro de la carpeta correspondiente.

### 🛡️ Wazuh

```text
labs_integrations/wazuh/
```

### 📊 Zabbix

```text
labs_integrations/zabbix/
```

### 🌐 Network / Deception

```text
labs_integrations/network_deception/
```

---

## 4. 🔍 Revisar cambios

```bash
git status
```

Para ver la rama actual:

```bash
git branch
```

Ejemplo:

```text
  main
* feature/wazuh-integration
```

---

## 5. ➕ Agregar cambios

```bash
git add .
```

También puedes agregar un archivo específico:

```bash
git add labs_integrations/wazuh/archivo.py
```

---

## 6. 💾 Crear commit

```bash
git commit -m "feat: add wazuh integration"
```

Ejemplos:

```bash
git commit -m "feat: add zabbix integration"
```

```bash
git commit -m "feat: add cowrie integration"
```

```bash
git commit -m "fix: update log analyzer"
```

```bash
git commit -m "docs: update wazuh documentation"
```

---

## 7. ☁️ Subir la rama a GitHub

```bash
git push origin feature/wazuh-integration
```

La primera vez también puedes utilizar:

```bash
git push -u origin feature/wazuh-integration
```

---

# 🔀 Pull Request

Después de subir la rama:

```text
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
```

No hacer merge directamente sin revisión.

---

# 🧪 Integración de herramientas

Las herramientas externas primero deben desarrollarse y probarse de manera independiente.

Ejemplo para Wazuh:

```text
🛡️ Wazuh
   ↓
🧪 Pruebas
   ↓
📁 labs_integrations/wazuh/
   ↓
✅ Validación
   ↓
🔀 Pull Request
   ↓
👨‍💻 Revisión
   ↓
🔗 Integración
   ↓
🤖 Sentinel Blue
```

Lo mismo aplica para Zabbix, Cowrie, TShark y otras herramientas.

---

# ⚠️ Archivos que NO deben subirse

No subir al repositorio:

```text
.env
venv/
__pycache__/
*.pyc
```

El archivo `.env` puede contener:

* 🔑 API Keys
* 🔐 Contraseñas
* 🎫 Tokens
* 🗄️ Credenciales de base de datos

Por seguridad, estas credenciales deben permanecer fuera del repositorio.

---

# 📋 Comandos rápidos

### 📥 Descargar

```bash
git clone <URL_DEL_REPOSITORIO>
```

### 📁 Entrar

```bash
cd sentinel-blue
```

### 🐍 Crear entorno

```bash
python3 -m venv venv
```

### ▶️ Activar Linux

```bash
source venv/bin/activate
```

### ▶️ Activar Windows

```bash
venv\Scripts\activate
```

### 📦 Instalar

```bash
pip install -r requirements.txt
```

### 🤖 Ejecutar agente

```bash
python cli.py
```

### ⚡ Ejecutar API

```bash
uvicorn backend.app.main:app --reload
```

### 🧪 Ejecutar pruebas

```bash
pytest
```

### 🔍 Ver estado

```bash
git status
```

### 🌿 Ver ramas

```bash
git branch
```

### 🔄 Actualizar `main`

```bash
git pull origin main
```

### 🌱 Crear rama

```bash
git checkout -b feature/nombre
```

### ➕ Agregar cambios

```bash
git add .
```

### 💾 Commit

```bash
git commit -m "descripcion"
```

### ☁️ Subir rama

```bash
git push origin feature/nombre
```

### 🔙 Volver a `main`

```bash
git checkout main
```

### 🛑 Desactivar entorno

```bash
deactivate
```

---

# 🛡️ Reglas principales

1. 🚫 No hacer `push` directamente a `main`.
2. 🌱 Cada integrante debe trabajar en su propia rama.
3. 🧪 Probar los cambios antes de crear un Pull Request.
4. 📁 Las nuevas integraciones comienzan en `labs_integrations/`.
5. 🤝 No modificar `agent/` o `backend/` sin coordinación con el Líder.
6. 🔐 Nunca subir credenciales o secretos.
7. 🔀 Todo cambio importante debe pasar por Pull Request.
8. 👨‍💻 El Líder revisará los cambios antes del merge.

---

# 🚀 Sentinel Blue

### 🤖 AI-Powered NOC/SOC Assistant

**Monitorizar → Analizar → Detectar → Investigar → Responder**

```

**Este formato te va a quedar mucho más limpio en GitHub** porque cada sección está separada y la estructura del proyecto está dentro de un bloque de código, en lugar de intentar construir todo el árbol en una sola línea como en tu captura.

