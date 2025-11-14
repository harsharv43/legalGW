# Legal Assistant Frontend

This is a React frontend for the Legal Assistant RAG system with PDF upload functionality.

## Features

- **PDF Upload Portal**: Interactive drag-and-drop interface for uploading legal documents
- **File Validation**: Ensures only PDF files are uploaded with a 10MB size limit
- **Real-time Feedback**: Upload progress indicators and success/error messages
- **Responsive Design**: Modern, professional UI with gradient background

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. The frontend will be available at `http://localhost:5173`

## Configuration

- The frontend expects the backend FastAPI server to be running on `http://localhost:8000`
- To change the API endpoint, update the `API_BASE_URL` constant in `src/components/PdfUpload.jsx`

## Usage

1. Make sure the backend server is running (see `../rag/README.md`)
2. Open the frontend in your browser
3. Drag and drop a PDF file or click to browse
4. Click "Upload File" to send the document to the backend
5. Uploaded files will be saved in the `../rag/data/` directory
