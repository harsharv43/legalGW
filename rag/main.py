from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = None

class GenerateDocRequest(BaseModel):
    doc_type: str
    context: Optional[str] = None

class GenerateDocResponse(BaseModel):
    document: str
    sources: Optional[List[str]] = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    # Placeholder logic
    return AskResponse(answer="This is a placeholder answer.", sources=["source1.pdf"])

@app.post("/generate-document", response_model=GenerateDocResponse)
def generate_document(request: GenerateDocRequest):
    # Placeholder logic
    return GenerateDocResponse(document="This is a placeholder document.", sources=["template1.docx"]) 