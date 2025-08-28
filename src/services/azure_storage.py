from azure.storage.blob import BlobServiceClient
import tempfile
import os
from core.config import settings

blob_service_client = BlobServiceClient.from_connection_string(settings.AZURE_STORAGE_CONNECTION_STRING)
def download_pdf(blob_name: str) -> str:
    blob_client = blob_service_client.get_blob_client(container="docs-container", blob=blob_name)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(blob_client.download_blob().readall())
        return tmp_file.name
