# test_api.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"[*] API Key cargada: {api_key[:8]}..." if api_key else "[!] NO HAY API KEY")

try:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Hola, responde únicamente con la palabra OK."
    )
    print(f"[+] Conexión exitosa con la API de Gemini. Respuesta: {response.text}")
except Exception as e:
    print(f"[!] Error de comunicación con la API de Gemini: {e}")