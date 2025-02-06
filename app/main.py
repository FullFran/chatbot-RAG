from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.chatbot import generar_respuesta

app = FastAPI()

# 🔹 Habilitar CORS para permitir conexiones desde GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fullfran.github.io"],  # Reemplaza con tu URL de GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configuración para renderizar plantillas HTML
templates = Jinja2Templates(directory="app/templates")

# Modelo de datos para recibir JSON
class ChatRequest(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    respuesta = generar_respuesta(request.query)
    return {"respuesta": respuesta}

