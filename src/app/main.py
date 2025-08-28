from fastapi import FastAPI
from routes import vectorize, query

app = FastAPI()

app.include_router(vectorize.router)
app.include_router(query.router)
