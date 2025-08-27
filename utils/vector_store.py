import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_faiss_index(text_chunks):
    # Create searchable database from resume chunks
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    resume_db = FAISS.from_texts(text_chunks, embedding=embeddings)
    resume_db.save_local("vector_store")
    return resume_db

