# Resume Analyzer

Built this to help recruiters search through multiple resumes quickly. Upload PDFs and either search across all of them or ask questions about specific candidates.

**Example queries:**
- "Which candidates know Python and machine learning?"
- "Who has worked at tech companies?"
- "Find someone with project management experience"
- "Show me senior developers with cloud experience"

## Setup

```bash
git clone <repo-url>
cd resume_qa_bot
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

Run the app:
```bash
streamlit run app.py
```

## Features

- Upload multiple PDF resumes
- Search across all resumes or query individual candidates
- Session-based isolation
- File size validation (10MB limit)
- Empty PDF detection

## Tech Stack

Python • Streamlit • Pinecone • Groq API • Sentence Transformers • PyMuPDF

## Architecture

The app uses a RAG (Retrieval-Augmented Generation) pipeline:

- PDFs are extracted and chunked (800 chars, 80 overlap)
- Text chunks are embedded using Sentence Transformers (all-MiniLM-L6-v2)
- Vectors stored in Pinecone with namespace isolation per session
- Multi-resume search uses cross-encoder reranking to improve precision
- Groq LLaMA-3.1 generates final responses

## Notes

- Free tier Pinecone and Groq API work fine for testing
- Tested with resumes up to 50+ pages
- Session namespaces prevent data leakage between users