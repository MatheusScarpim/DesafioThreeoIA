import os

class Settings:
    AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=edatajanus;AccountKey=W5y7X1c84AHm8BSBwM0DJPy6KWIHm6HI;EndpointSuffix=core.windows.net"
    AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "docs-container")
    QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "pdf_collection")

settings = Settings()
