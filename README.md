# Smart Resume Q&A Chatbot

> **A production-ready RAG system that intelligently answers questions about your resume using advanced NLP techniques.**

Built this to solve the problem of quickly extracting specific information from resumes during interviews and applications. Instead of manually searching through documents, just ask natural language questions and get instant, accurate answers.

**Try asking:**
- "What programming languages do I know?"
- "Where did I complete my education?"
- "What projects have I worked on?"
- "What are my key achievements?"

## 🎬 Demo

![Demo GIF](demo.gif)

*Upload your resume and start asking questions instantly!*

---

## 🏗️ Architecture

**RAG Pipeline:** PDF → Text Extraction → Chunking → Vector Embeddings → Semantic Search → LLM Generation

```
PDF Upload → PyMuPDF → LangChain Splitter → HuggingFace Embeddings → FAISS Index
                                                                        ↓
User Query → Vector Search → Context Retrieval → Groq LLaMA-4 → Answer
```

## 🛠️ Tech Stack

- **Backend:** Python, LangChain
- **Vector DB:** FAISS (local, fast)
- **LLM:** Groq's LLaMA-4 (free, fast inference)
- **Embeddings:** HuggingFace Sentence Transformers
- **PDF Processing:** PyMuPDF
- **Frontend:** Streamlit
- **Deployment:** Local/Cloud ready

## ⚡ Features

- **Smart PDF Processing:** Handles complex resume layouts
- **Semantic Search:** Finds relevant info even with different wording
- **Context-Aware Answers:** Uses RAG for accurate, grounded responses
- **Cost-Effective:** Uses free Groq API instead of expensive OpenAI
- **Error Handling:** Robust validation and user-friendly error messages
- **Professional UI:** Clean Streamlit interface

## Quick Start

1. **Clone & Install**
```bash
git clone <repo-url>
cd resume_qa_bot
pip install -r requirements.txt
```

2. **Setup API Key**
```bash
# Create .env file
echo "GROQ_API_KEY=your_groq_api_key" > .env
```

3. **Run**
```bash
streamlit run app.py
```

## 📈 Future Roadmap

### Stage 2: Enhanced Flexibility (Next Week)
- **Multi-Model Support:** Dropdown to switch between Groq, HuggingFace models
- **Advanced Error Handling:** Support password-protected PDFs, better validation
- **UI/UX Improvements:** Better loading states, file preview
- **Model Comparison:** Side-by-side answer comparison

### Stage 3: Production-Grade RAG (Next Month)
- **Reranker Integration:** Cohere/cross-encoder for better retrieval accuracy
- **Advanced Retrieval:** Hybrid search (keyword + semantic)
- **Performance Analytics:** Response time monitoring, accuracy metrics
- **Scalability:** Support multiple documents, user sessions

##  Technical Highlights

- **RAG Architecture:** Implemented end-to-end retrieval-augmented generation
- **Vector Search:** FAISS for sub-second semantic similarity search
- **Chunking Strategy:** Optimized 800-char chunks with 80-char overlap
- **API Integration:** OpenAI-compatible interface with Groq backend
- **Error Resilience:** Comprehensive exception handling throughout pipeline

## 📊 Performance

- **Response Time:** < 3 seconds for most queries
- **Accuracy:** High relevance due to semantic search + context
- **Cost:** $0 (using free Groq API)
- **Scalability:** Handles resumes up to 50+ pages

---

**Built with ❤️ for efficient resume analysis and interview preparation.**