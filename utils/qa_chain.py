from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from utils.groq_llm import ask_groq as ask_model  #  Using Groq

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("vector_store", embeddings, allow_dangerous_deserialization=True)

def answer_question(query):
    vectorstore = load_vectorstore()
    docs = vectorstore.similarity_search(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"""Use the following resume content to answer the question.\n\nResume:\n{context}\n\nQuestion: {query}"""
    return ask_model(prompt)
