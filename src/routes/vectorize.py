from fastapi import APIRouter
from models.request_models import VectorizeRequest
from services.rag_service import process_document

router = APIRouter()

@router.post("/vectorize")
async def vectorize_endpoint(request: VectorizeRequest):
    result = await process_document(request.blob_name)
    return result