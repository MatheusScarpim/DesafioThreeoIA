from pydantic import BaseModel

class VectorizeRequest(BaseModel):
    blob_name: str

class QueryRequest(BaseModel):
    question: str
