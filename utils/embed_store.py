import os
import faiss
import pickle
from langchain_community.embeddings import HuggingFaceEmbeddings




from langchain_community.vectorstores import FAISS
#
# from dotenv import load_dotenv
#
# load_dotenv()

def create_faiss_index(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    vectorstore.save_local("../vector_store")
    return vectorstore


# from utils.extract_text import extract_text_from_pdf
# from utils.text_splitter import split_text_into_chunks
#
# text = extract_text_from_pdf("../resume.pdf")
# chunks = split_text_into_chunks(text)
# create_faiss_index(chunks)  # Should now work using HuggingFace

