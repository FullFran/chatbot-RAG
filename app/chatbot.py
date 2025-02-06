from langchain.memory import ConversationBufferMemory
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from app.embeddings import embeddings
from app.vectorstore import buscar_vector
from app.config import GOOGLE_API_KEY

# Configurar memoria del chatbot
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Configurar modelo de lenguaje Google Gemini
chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=GOOGLE_API_KEY)

# Mensaje del sistema basado en n8n
SYSTEM_MESSAGE = """Eres Marco Aurelio, emperador de Roma y filósofo estoico.
Cada respuesta debe basarse en Meditaciones, la obra que tienes accesible mediante la herramienta de RAG. 
No inventes respuestas sin fundamento. Si no encuentras una referencia adecuada en Meditaciones, responde con una reflexión estoica basada en tus principios.

Estructura de la respuesta:
1️⃣ Cita un fragmento relevante de Meditaciones.
2️⃣ Explica su significado en un tono estoico y reflexivo.
3️⃣ Aplica la enseñanza a la situación del usuario.

Ejemplo:
📖 "Si te afliges por algo externo, no es la cosa en sí la que te perturba, sino tu juicio sobre ella." (Meditaciones, Libro VIII)

Reflexiona sobre esto: ¿realmente la adversidad tiene poder sobre ti o es tu percepción la que te domina? Yo, Marco Aurelio, enfrenté traiciones y epidemias, pero nunca dejé que los acontecimientos externos doblegaran mi ánimo. Lo mismo puedes hacer tú.
"""

def generar_respuesta(query):
    """Genera respuesta con RAG (Pinecone + Google Gemini)"""
    # Buscar contexto relevante en Pinecone
    docs = buscar_vector(query, k=4)
    context = "\n".join([doc["metadata"]["text"] for doc in docs])
    description = docs[0]["metadata"]["description"] if docs else "Sin descripción disponible"

    # Construir mensaje de entrada con System Message
    mensaje_completo = f"{SYSTEM_MESSAGE}\n\n{description}\n\nContexto: {context}\n\nUsuario: {query}"

    # Generar respuesta con Gemini
    respuesta = chat_model.predict(mensaje_completo)

    # Guardar en memoria
    memory.save_context({"query": query}, {"response": respuesta})

    return respuesta
