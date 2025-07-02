# Legal Assistant RAG Backend

This backend powers a Retrieval-Augmented Generation (RAG) system for legal Q&A and document generation for Indian startups/SMBs.

## Features
- Legal Q&A using public laws, templates, and policy PDFs
- Document generation (contracts, compliance checklists)
- Source citation
- API endpoints for frontend/SaaS integration

## Stack
- Python (FastAPI)
- LangChain (RAG orchestration)
- OpenAI (embeddings, LLM)
- ChromaDB (vector store)
- Basic scraper for indiacode.nic.in

## Setup
1. `pip install -r requirements.txt`
2. Add your OpenAI API key as `OPENAI_API_KEY` in your environment
3. Run the backend: `uvicorn main:app --reload`

## Endpoints
- `/ask` — Legal Q&A
- `/generate-document` — Document drafting

## Data
- Place legal docs, templates, and PDFs in `data/`

--- 