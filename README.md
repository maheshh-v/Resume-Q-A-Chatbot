#  Smart Resume Q&A Chatbot (LangChain + FAISS + LLaMA-4)

A smart chatbot that answers questions about your resume using LLM + vector search. Built using LangChain, FAISS, and **Groq’s LLaMA-4 model** via an OpenAI-compatible API. You can ask queries like:

- "What is my CGPA?"  
- "What skills do I have?"  
- "Where did I study?"  
- "In which areas am I still growing?"

---

## 🔧 Tech Stack

- Python  
- LangChain  
- FAISS (Vector Database)  
- LLaMA-4 via [Groq API](https://groq.com)  
- PyMuPDF (PDF parsing)  
- Streamlit (Web UI)

---

## 📁 Features

- ✅ Resume PDF upload and processing  
- ✅ PDF text extraction and chunking  
- ✅ Vector embedding using Sentence Transformers  
- ✅ Semantic search using FAISS  
- ✅ Q&A using LLaMA-4 via Groq’s OpenAI-compatible API  
- ✅ Simple Streamlit interface  
- ✅ No OpenAI API key or credit needed

---

## 🆕 Recent Update

> 🔁 **Switched from OpenAI to Groq’s LLaMA-4 (Meta) for free usage.**
>
> - Uses [Groq’s API](https://console.groq.com) instead of paid OpenAI keys  
> - Fully compatible with `openai.ChatCompletion` format  
> - Smart, cost-efficient LLM usage

---

##  Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Make sure to:

*   Set your Groq API key in an `.env` file or inside `groq_llm.py` like:
    
    python
    
    CopyEdit
    
    `api_key = "your-groq-key"`
    

* * *

## What I Learned

*   How to build a Retrieval-Augmented Generation (RAG) system
    
*   How to use FAISS for semantic vector search
    
*   How to embed documents and search them meaningfully
    
*   How to use Groq's OpenAI-compatible LLM APIs
    
*   End-to-end ML project thinking: from PDF to chatbot
    
*   Cost-saving strategies using free APIs instead of paid ones
    

* * *
