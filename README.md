# Resume Analyzer

Built this to help recruiters search through multiple resumes quickly. Upload PDFs and either search across all of them or ask questions about specific candidates.

**What you can do:**
- "Which candidates know Python and machine learning?"
- "Who has worked at tech companies?"
- "Find someone with project management experience"
- "Show me senior developers with cloud experience"

## How to Run

1. **Install dependencies**
```bash
git clone <repo-url>
cd resume_qa_bot
pip install -r requirements.txt
```

2. **Set up API key**
```bash
# Create .env file
echo "GROQ_API_KEY=your_groq_api_key" > .env
```

3. **Start the application**
```bash
streamlit run app.py
```

## Features

- Upload multiple PDF resumes at once
- Search through all resumes to find matching candidates
- Ask specific questions about individual resumes
- Delete individual files or clear all at once
- Session-based isolation for multiple users

## Tech Stack

- **Backend:** Python, LangChain
- **Database:** Pinecone vector database
- **LLM:** Groq API
- **Text Processing:** PyMuPDF, Sentence Transformers
- **Frontend:** Streamlit

## How It Works

1. Upload PDF resumes
2. Text gets extracted and stored in Pinecone vector database
3. Two search modes:
   - **Search all resumes:** Find candidates matching job requirements
   - **Single resume Q&A:** Ask questions about one specific person

## Technical Details

**RAG Pipeline:**
- Text extraction from PDFs using PyMuPDF
- Chunking with LangChain (800 chars, 80 overlap)
- Vector embeddings via Sentence Transformers
- Pinecone storage with session-based namespaces
- MMR retrieval for diverse results across resumes
- Cross-encoder reranking for precision
- Groq LLaMA-3.1 for final synthesis

**Key Implementation Decisions:**
- Used MMR to prevent single resume bias in search results
- Added reranker to improve context quality before LLM
- Session namespaces ensure user data isolation

## Notes

- Uses Pinecone for vector storage (free tier works fine)
- Groq API for LLM responses (faster and free compared to OpenAI)
- Supports large resumes (tested up to 50+ pages)