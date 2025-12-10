# Agente IA Especialista en DevOps (LangGraph + Gemini)

Este proyecto implementa un agente inteligente modular utilizando **LangGraph** para el flujo de estado y **Google Gemini (2.5 Flash)** como motor de razonamiento.

El agente actúa con una arquitectura de **"Analista + Experto"**:
1.  **Analiza** la consulta del usuario para determinar su intención y validar el dominio.
2.  **Filtra** preguntas fuera de contexto (Guardrails).
3.  **Responde** como un experto técnico si la consulta es válida.

---

## Requisitos Previos

Antes de empezar, asegúrate de tener instalado:

* **Python 3.10 o superior** (Recomendado 3.11/3.12 para evitar conflictos de SSL en macOS).
* **Git**.
* Una **API Key de Google Gemini** (Obtenla gratis en [Google AI Studio](https://aistudio.google.com/)).
* **VS Code** (Recomendado).

---

## Instalación y Configuración

Sigue estos pasos para configurar el proyecto en tu entorno local.

### 1. Clonar el repositorio

```bash
git clone https://github.com/GustavoOspinaL/laboratorio1-IA.git
cd Laboratorio1
```

### 2. Crear un Entorno Virtual
En macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno (API Key)
Por seguridad, las claves no se incluyen en el código.
Crea un archivo llamado .env en la raíz del proyecto (al mismo nivel que main.py).
Agrega tu clave API dentro del archivo con el siguiente formato:

```plaintext
GOOGLE_API_KEY=tu_clave_api_aqui_pegada_sin_comillas
```

### 5. Ejecución
```bash
python main.py
```