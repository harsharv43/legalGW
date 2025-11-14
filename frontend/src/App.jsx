import { useState } from 'react'
import './App.css'
import PdfUpload from './components/PdfUpload'

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Legal Assistant</h1>
        <p>Upload legal documents and PDFs for processing</p>
      </header>
      <main className="app-main">
        <PdfUpload />
      </main>
    </div>
  )
}

export default App
