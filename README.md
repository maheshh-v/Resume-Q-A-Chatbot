# Resume Analyzer

A RAG-based application to help recruiters search through multiple resumes efficiently. Upload PDF resumes and search across all of them or ask questions about specific candidates.

**[Watch Demo](https://youtu.be/y-PEmwMbuWk)**

**Example queries:**
- "Which candidates know Python and machine learning?"
- "Who has experience at tech companies?"
- "Find someone with project management skills"
- "Show me developers with cloud experience"

## Installation

```bash
git clone https://github.com/maheshh-v/Resume-Q-A-Chatbot.git
cd Resume-Q-A-Chatbot
pip install -r requirements.txt
```

Create `.env` file in the root directory:
```
GROQ_API_KEY=your_api_key_here
PINECONE_API_KEY=your_api_key_here
```

Start the application:
```bash
streamlit run app.py
```

## Features

- Multi-file PDF upload support
- Cross-resume search with candidate comparison
- Individual resume Q&A
- Session isolation for concurrent users
- File validation (10MB limit, empty PDF detection)

## Tech Stack

Python • Streamlit • LangChain • Pinecone • Groq API • Sentence Transformers • PyMuPDF

## How It Works

RAG pipeline implementation:

- PDF text extraction and chunking (800 char chunks, 80 char overlap)
- Embeddings generated using Sentence Transformers (all-MiniLM-L6-v2)
- Vector storage in Pinecone with session-based namespace isolation
- Cross-encoder reranking for improved multi-resume search accuracy
- Response generation via Groq LLaMA-3.1

## Notes

- Compatible with Pinecone and Groq free tiers
- Handles large resumes (tested up to 50+ pages)
- Namespace isolation ensures user data privacy