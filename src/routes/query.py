from fastapi import APIRouter
from models.request_models import QueryRequest
from services.rag_service import query_rag

router = APIRouter()

@router.post("/query")
async def query_endpoint(request: QueryRequest):
    result = await query_rag(request.question)
    return result