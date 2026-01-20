from fastapi import FastAPI
from pydantic import BaseModel
from helpers.chromadb import init_vector_store, query
from helpers.llm import generate_response

app = FastAPI()

vector_store= init_vector_store()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class QueryRequest(BaseModel):
    question: str
    top_k:int = 2


@app.post('/query')
def search_db(request: QueryRequest):
    results = query(request.question, vector_store=vector_store, top_k=request.top_k)
    return results

@app.post('/chat')
def chat(request: QueryRequest):
    results = query(request.question, vector_store=vector_store, top_k=request.top_k)
    response=generate_response("Question:{user_question}")
    return response