
import os
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from utils.llm_client import ask_groq as ask_model

def load_vectorstore():
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        return FAISS.load_local("vector_store", embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        raise FileNotFoundError(f"Vector store not found. Please upload a resume first. Error: {str(e)}")

def answer_question(user_query):
    try:
        resume_db = load_vectorstore()
        relevant_sections = resume_db.similarity_search(user_query)
        
        if not relevant_sections:
            return "I couldn't find relevant information in your resume to answer this question."
        
        # Combine relevant resume sections
        resume_context = "\n\n".join([section.page_content for section in relevant_sections])
        prompt = f"""Use the following resume content to answer the question.\n\nResume:\n{resume_context}\n\nQuestion: {user_query}"""
        return ask_model(prompt)
    except Exception as e:
        return f"Error processing your question: {str(e)}"
