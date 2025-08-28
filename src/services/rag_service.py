from core.config import settings
from services.azure_storage import download_pdf
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from qdrant_client import QdrantClient

import os

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

QDRANT_URL = settings.QDRANT_URL
collection_name = settings.COLLECTION_NAME

qdrant_client = QdrantClient(url=QDRANT_URL)

def create_collection_if_not_exists(qdrant_client, collection_name, dim=384):
    if not qdrant_client.collection_exists(collection_name):
        qdrant_client.create_collection(
            collection_name,
            vectors_config={"size": dim, "distance": "Cosine"}
        )
        print(f"Coleção '{collection_name}' criada com sucesso com vetores de {dim} dimensões.")
    else:
        print(f"Coleção '{collection_name}' já existe.")
    
vectorstore = Qdrant(
    client=qdrant_client,
    collection_name=collection_name,
    embeddings=embeddings
)

llm = OllamaLLM(model=settings.LLM_NAME, base_url=settings.OLLAMA_URL)

prompt_template = """Use o contexto abaixo para responder à pergunta. 
Se não souber, diga que não sabe.

Contexto:
{context}

Pergunta:
{question}

Na Resposta não coloque que você tem um contexto.
Resposta:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

async def process_document(blob_name: str):
    create_collection_if_not_exists(qdrant_client, collection_name)
    local_path = download_pdf(blob_name)
    loader = PyPDFLoader(local_path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(pages)
    vectorstore.add_documents(chunks)
    os.remove(local_path)
    return {"status": "ok", "chunks_added": len(chunks)}

async def query_rag(question: str):
    create_collection_if_not_exists(qdrant_client, collection_name)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )
    result = qa_chain.run(question)
    return {"answer": result}