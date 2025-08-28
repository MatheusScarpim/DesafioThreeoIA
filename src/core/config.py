import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "docs-container")
    QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "pdf_collection_v3")
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
    LLM_NAME = os.getenv("LLM_NAME", "llama3:8b")

settings = Settings()