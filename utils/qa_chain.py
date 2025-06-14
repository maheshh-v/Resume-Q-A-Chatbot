from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("../vector_store", embeddings, allow_dangerous_deserialization=True)

def load_llm():
    qa_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        tokenizer="google/flan-t5-small",
        max_length=512
    )
    return HuggingFacePipeline(pipeline=qa_pipeline)

def answer_question(query):
    # Load vector store and relevant docs
    vectorstore = load_vectorstore()
    docs = vectorstore.similarity_search(query)

    # Load local LLM and QA chain
    llm = load_llm()
    chain = load_qa_chain(llm, chain_type="stuff")

    # Run chain with query
    response = chain.run(input_documents=docs, question=query)
    return response

# response = answer_question("What programming languages do I know?")
# print("Answer:", response)