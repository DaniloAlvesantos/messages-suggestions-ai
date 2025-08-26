from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://bjkcdchdaniilnidjmgmekfaijipdhhe", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_API_URL = "http://localhost:11434/api/generate" 
OLLAMA_MODEL = "llama3.2:1b"

class GenerateRequest(BaseModel):
    prompt: str 

# 1 - source .venv/bin/activate; ( local )
# 2 - fastapi dev app.py
@app.post("/generate")
def generate(request: GenerateRequest):
    prompt_text = (
        "You are a WhatsApp assistant. "
        "Always reply exclusively with a JSON array containing exactly 3 short, polite, and friendly message suggestions in Brazilian Portuguese. "
        "The tone should be welcoming, natural, and professional, as in a customer service conversation. "
        "Example: ['Oiee, como vai? 🥰', 'Claro, temos sim!', 'Boa Tarde, como posso ajudar? 🥰']. "
        f"User message: '{request.prompt}'"
    )

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt_text,
        "stream": False,
       "format": {
            "type": "object",
            "properties": {
                "0": { "type": "string" },
                "1": { "type": "string" },
                "2": { "type": "string" }
            },
            "required": ["0", "1", "2"]
        }
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
    except Exception as e:
        print("Error calling Ollama API:", e)
        return {"error": str(e)}

    data = response.json()

    route_response = {
        "suggestions": data.get("response"),
        "original_message": request.prompt
    }

    return route_response
