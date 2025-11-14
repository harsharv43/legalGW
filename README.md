# legalGW

Legal Assistant - A RAG-based system for legal Q&A and document generation with interactive PDF upload portal.

## Features

- **PDF Upload Portal**: React-based frontend for uploading legal documents
- **Legal Q&A**: Ask questions about legal matters using RAG
- **Document Generation**: Generate legal documents and contracts
- **FastAPI Backend**: RESTful API for processing and storage

## Quick Start

### Backend
```bash
cd rag
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173` to access the PDF upload portal.