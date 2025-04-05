import pinecone
from app.config import PINECONE_API_KEY, PINECONE_INDEX, PINECONE_ENVIRONMENT
from app.embeddings import embeddings

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
index = pc.Index(PINECONE_INDEX)

# Descripción de la base de datos
DATA_DESCRIPTION = "Esta base contiene fragmentos de Meditaciones de Marco Aurelio. Usa esta información como referencia primaria en cada respuesta."

def indexar_documento(texto, id):
    """Almacena fragmentos en Pinecone con metadata y embeddings."""
    vector = embeddings.embed_query(texto)
    metadata = {"text": texto, "description": DATA_DESCRIPTION}
    index.upsert(vectors=[{"id": id, "values": vector, "metadata": metadata}])

def buscar_vector(query, k=4):
    """Busca fragmentos relevantes en Pinecone."""
    vector = embeddings.embed_query(query)
    results = index.query(vector=vector, top_k=k, include_metadata=True)
    
    # Agregar la descripción a cada resultado
    for match in results["matches"]:
        match["metadata"]["description"] = DATA_DESCRIPTION

    return results["matches"]
