from azure.storage.blob import BlobServiceClient
import tempfile
import os
from core.config import settings

blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=edatajanus;AccountKey=3qQH5RjeiDSeHB91qVWFq6CbWysxWGEsxQ57Q1xGWBQJ8nnjyngDwFp5WohlmrO2WQuhGmwR3JqO+AStHf3qsQ==;EndpointSuffix=core.windows.net")
def download_pdf(blob_name: str) -> str:
    blob_client = blob_service_client.get_blob_client(container="docs-container", blob=blob_name)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(blob_client.download_blob().readall())
        return tmp_file.name
