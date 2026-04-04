import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings

load_dotenv()
OLLAMA_IP = os.getenv("OLLAMA_PROVIDER_IP")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text", base_url=f"http://{OLLAMA_IP}:11434"
)
