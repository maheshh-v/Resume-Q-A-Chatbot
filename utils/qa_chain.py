from langchain_pinecone import PineconeVectorStore
from utils.pinecone_client import get_or_create_index
from langchain_huggingface import HuggingFaceEmbeddings
from utils.llm_client import ask_groq as ask_model
from sentence_transformers import CrossEncoder
import streamlit as st

@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def load_pinecone_vectorstore(namespace: str):
    embeddings = get_embeddings()
    pinecone_index = get_or_create_index()
    vectorstore = PineconeVectorStore(
        index=pinecone_index, 
        embedding=embeddings, 
        namespace=namespace,
        text_key='text'
    )
    return vectorstore

def answer_question(user_query, selected_resume=None, namespace=None, k=5):
    try:
        resume_db = load_pinecone_vectorstore(namespace)

        if selected_resume:
            # Fetch more results and filter manually
            all_results = resume_db.similarity_search(
                user_query, 
                k=50,
                namespace=namespace
            )
            relevant_sections = [doc for doc in all_results if doc.metadata.get('source') == selected_resume][:k]
        else:
            relevant_sections = resume_db.similarity_search(
                user_query, 
                k=k,
                namespace=namespace
            )

        if not relevant_sections:
            return f"No relevant information found in {selected_resume or 'the uploaded resumes'}"
        
        context = ""
        for doc in relevant_sections:
            source = doc.metadata.get('source', 'Unknown File')
            context += f"[{source}]\n{doc.page_content}\n\n"
        
        prompt = f"""Answer the question based on the resume snippets below. Focus on the specific candidate mentioned in the source file.

Resume Snippets:
{context}

Question: {user_query}

Answer:"""

        return ask_model(prompt)

    except Exception as e:
        print(f"Error in answer_question: {e}")
        return f"Error processing question: {str(e)}"

@st.cache_resource
def load_reranker_model():
    return CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def perform_recruiter_search(query: str, namespace: str):
    resume_db = load_pinecone_vectorstore(namespace)
    # Use similarity_search with namespace parameter directly
    relevant_sections = resume_db.similarity_search(
        query,
        k=20,
        namespace=namespace
    )

    if not relevant_sections:
        return "No relevant information was found in any of the uploaded resumes."
    
    # rerank for precision
    reranker_model = load_reranker_model()
    passages = [doc.page_content for doc in relevant_sections]
    reranker_input = [[query, passage] for passage in passages]
    
    scores = reranker_model.predict(reranker_input)
    reranked_docs = sorted(zip(scores, relevant_sections), key=lambda x: x[0], reverse=True)
    top_docs = [doc for score, doc in reranked_docs[:7]]
    context = ""
    for doc in top_docs:
        source = doc.metadata.get('source', 'Unknown File')
        context += f"[{source}]\n{doc.page_content}\n\n"

    prompt = f"""Analyze these resume snippets and identify candidates matching the requirements. Compare their qualifications and explain why they're a good fit.

Requirements:
{query}

Resume Snippets:
{context}

Analysis:"""

    return ask_model(prompt)