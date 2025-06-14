# 🧠 Smart Resume Q&A Chatbot (LangChain + FAISS)

A smart chatbot that answers questions about your resume using LLM + vector search. Built using LangChain, FAISS, and OpenAI/HuggingFace models. You can ask queries like:

- "What is my CGPA?"  
- "What skills do I have?"  
- "Where did I study?"

## 🔧 Tech Stack

- Python
- LangChain
- FAISS (Vector DB)
- Hugging Face Transformers / OpenAI
- PyMuPDF (PDF parsing)
- Streamlit (Web UI)

## 📁 Features

- PDF text extraction and chunking  
- Vector embedding with OpenAI or FLAN-T5  
- Semantic search using FAISS  
- Q&A via LangChain Retrieval Chain  
- Simple Streamlit UI for interaction

[//]: # (## 📷 Screenshots)



## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📝 What I Learned

*   How to build a Retrieval-Augmented Generation (RAG) system
    
*   How to use FAISS for vector search
    
*   How to chain prompts and embed document context
    
*   Basics of LLM integration with LangChain
    
*   End-to-end project thinking (from resume to deployed chatbot)

