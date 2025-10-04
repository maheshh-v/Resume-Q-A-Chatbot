from langchain_pinecone import PineconeVectorStore
from utils.pinecone_Vector_DB import get_or_create_index
from langchain_huggingface import HuggingFaceEmbeddings
from utils.llm_client import ask_groq as ask_model
from sentence_transformers import CrossEncoder
import streamlit as st
import uuid

def load_pinecone_vectorstore(namespace: str):
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        pinecone_index = get_or_create_index()
        vectorstore = PineconeVectorStore(
            index=pinecone_index, 
            embedding=embeddings, 
            namespace=namespace
        )
        return vectorstore
    except Exception as e:
        raise ConnectionError(f"Could not connect to Pinecone vector store. Error: {str(e)}")

def answer_question(user_query, selected_resume=None, namespace=None, k=5):
    try:
        resume_db = load_pinecone_vectorstore(namespace)

        if selected_resume:
            relevant_sections = resume_db.similarity_search(
                user_query,
                k=k,
                filter={"source": selected_resume}
            )
        else:
            relevant_sections = resume_db.similarity_search(user_query, k=k)

        if not relevant_sections:
            return f"Can't find that info in {selected_resume or 'your resume(s)'}"
        
        context = ""
        for doc in relevant_sections:
            source = doc.metadata.get('source', 'Unknown File')
            context += (
                f"--- Start of Snippet from {source} ---\n"
                f"{doc.page_content}\n"
                f"--- End of Snippet from {source} ---\n\n"
            )
        
        prompt = f"""You are an HR assistant. 
Your job is to answer questions based ONLY on the resume snippets provided below. 
Pay close attention to the source file mentioned for each snippet to avoid mixing up information between different people.

Contexts:
{context}

Question: {user_query}

Answer:"""

        return ask_model(prompt)

    except Exception as e:
        error_id = str(uuid.uuid4())[:8]
        print(f"Error [{error_id}] in answer_question: {e}")
        return f"Unable to process your question. If this persists, please report error ID: {error_id}"

@st.cache_resource
def load_reranker_model():
    return CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def perform_recruiter_search(query: str, namespace: str):
    resume_db = load_pinecone_vectorstore(namespace)
    # Fetch 50 docs, select top 20 diverse results using MMR
    retriever = resume_db.as_retriever(
        search_type="mmr",
        search_kwargs={'k': 20, 'fetch_k': 50}
    )
    relevant_sections = retriever.get_relevant_documents(query)

    if not relevant_sections:
        return "No relevant information was found in any of the uploaded resumes."
    
    # Rerank results for better accuracy
    reranker_model = load_reranker_model()
    passages = [doc.page_content for doc in relevant_sections]
    reranker_input = [[query, passage] for passage in passages]
    
    scores = reranker_model.predict(reranker_input)
    reranked_docs = sorted(zip(scores, relevant_sections), reverse=True)
    top_docs = [doc for score, doc in reranked_docs[:7]]
    context = ""
    for i, doc in enumerate(top_docs):
        source = doc.metadata.get('source', 'Unknown File')
        context += f"--- Snippet {i+1} from {source} ---\n"
        context += doc.page_content
        context += f"\n---\n\n"

    prompt = f"""You are an HR analyst and talent sourcer. Your task is to analyze the following resume snippets from multiple candidates and synthesize an answer to the user's query.
    
    Carefully review the user's query and the provided resume snippets. Identify the most qualified candidates who match the requirements. If the query is a job description, list the best candidates and provide a detailed justification for each, explaining how their skills and experience align with the role.

    If multiple candidates are relevant, compare their qualifications. Do not just list facts; provide a clear, concise, and actionable analysis.

    User Query / Job Description:
    {query}

    Resume Snippets:
    {context}

    ---
    INSTRUCTIONS:
    Synthesize a clean, professional report comparing the top candidates based on the snippets above. Your final output should only contain sections for the top candidates and a final comparison. Do not create a separate section analyzing the individual snippets themselves.

    Analysis:"""

    return ask_model(prompt)