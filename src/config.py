import os
from dotenv import load_dotenv

# Cargar variables de .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("no se pudo cargar GOOGLE_API_KEY del archivo .env")

# --- Configuración MySQL ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "3306")

MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.3
DOMAIN = "DevOps"