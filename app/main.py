from fastapi import FastAPI
from app.chatbot import generar_respuesta

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(query: str):
    respuesta = generar_respuesta(query)
    return {"respuesta": respuesta}
