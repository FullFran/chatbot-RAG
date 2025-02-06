# **Chatbot RAG - Marco Aurelio** 🏛️🤖  
_A conversational AI chatbot based on Retrieval-Augmented Generation (RAG), inspired by the Stoic philosophy of Marcus Aurelius._
Robust and scalable RAG chatbot designed to integrate advanced AI capabilities for intelligent question-answering. This project leverages cutting-edge natural language processing (NLP) and vector search technologies to enhance the chatbot's accuracy and efficiency.

## **📜 Overview**
Chatbot RAG is an AI-powered conversational assistant designed to emulate Marcus Aurelius' philosophy. It uses **FastAPI** for the backend, **LangChain** for retrieval-augmented generation (RAG), and is deployed across **Railway (backend)** and **GitHub Pages (frontend)**.

---

## **🚀 Features**
✔ **Retrieval-Augmented Generation (RAG):** Generates answers based on Marcus Aurelius' *Meditations*.  

✔ **FastAPI Backend:** High-performance, asynchronous API framework for handling chatbot interactions.

✔ **LangChain Integration:** Modular framework for integrating Large Language Models (LLMs) with external data sources.  

✔ **Pinecone Vector Search:** Retrieves relevant quotes from *Meditations*.  

✔ **Lightweight Frontend:** Deployed on GitHub Pages with a simple HTML/CSS/JS interface.  

✔ Docker - Containerized deployment ensuring scalability and easy integration.

✔ **Cloud Deployment:** Backend on Railway, frontend on GitHub Pages.  

---

## **📂 Repository Structure**
```
/chatbot-RAG
  ├── app/                  # Backend (FastAPI + LangChain)
  │   ├── chatbot.py        # Chat logic (RAG + LangChain)
  │   ├── config.py         # Environment variables
  │   ├── embeddings.py     # Google AI embeddings
  │   ├── main.py           # FastAPI app
  │   ├── vectorstore.py    # Pinecone vector search
  │   ├── requirements.txt  # Dependencies
  ├── docs/                 # Frontend (GitHub Pages)
  │   ├── index.html        # Web UI
  │   ├── styles.css        # Chat styling
  │   ├── script.js         # Handles chat interactions
  ├── .env                  # Environment variables (ignored)
  ├── .gitignore            # Ignore unnecessary files
  ├── Dockerfile            # Docker configuration for deployment
  ├── README.md             # Project documentation
```

---

## **🛠 Installation**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/FullFran/chatbot-RAG.git
cd chatbot-RAG
```

### **2️⃣ Set up the backend**
#### **Using Docker (Recommended)**
```bash
docker build -t chatbot-rag .
docker run -p 8000:8000 chatbot-rag
```
#### **Manual Setup**
```bash
pip install -r app/requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## **📡 Deployment**
### **Backend: Railway**
The backend is deployed on **Railway**. To redeploy, push changes to the `main` branch.
```bash
git add .
git commit -m "Updated backend"
git push origin main
```
Railway will automatically detect and deploy updates.

---

### **Frontend: GitHub Pages**
The frontend is served via **GitHub Pages**.  
To update, modify the files in the `docs/` folder and push changes.

---

## **📌 Usage**
1️⃣ **Open the Chatbot:** [`https://fullfran.github.io/chatbot-RAG/`](https://fullfran.github.io/chatbot-RAG/)  

2️⃣ **Type a question related to Stoicism.**  

3️⃣ **Receive an answer based on *Meditations* by Marcus Aurelius.**  

---

## **🌍 Environment Variables**
The project requires the following **.env** variables (not included in the repo):
```env
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=us-east1-gcp
PINECONE_INDEX=marcoaurelio
```

## API Endpoints

The chatbot API provides endpoints for querying the RAG model:

- POST /chat - Sends a user query and retrieves an AI-generated response.

- POST /ingest - Indexes new documents into the vector database.

## Technology Stack & Relevant Expertise

This project demonstrates expertise in:

### Backend Development

- FastAPI: Async API development with dependency injection and Pydantic validation.

- Docker & Docker Compose: Containerization for seamless deployment.


### AI & NLP

- LangChain: LLM orchestration with advanced prompt engineering.

- OpenAI API: Integration of GPT-based language models.

- Pinecone: High-performance vector search for information retrieval.

### DevOps & Cloud

- Containerization: Deployment-ready with Docker.

- Scalability: Microservices-based architecture ensuring extensibility.

- Cloud AI Integration: Leveraging cloud-based AI APIs for enhanced performance.





