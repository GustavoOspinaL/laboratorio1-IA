import os
from dotenv import load_dotenv

# Cargar variables de .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("no se pudo cargar GOOGLE_API_KEY del archivo .env")

MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.3
DOMAIN = "DevOps"