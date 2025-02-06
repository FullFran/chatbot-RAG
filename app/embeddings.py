from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", api_key=GOOGLE_API_KEY)
