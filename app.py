import streamlit as st
from utils.text_extraction import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import create_faiss_index
from utils.qa_chain import answer_question
import os
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables 
st.set_page_config(page_title="Smart Resume Q&A", layout="centered")

st.title("📄 Smart Resume Q&A Chatbot")
st.write("Upload your resume and ask questions about it!")

# Upload section
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file:
    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("Resume uploaded successfully!")

    # Process resume for Q&A
    resume_text = extract_text_from_pdf("resume.pdf")
    text_chunks = split_text_into_chunks(resume_text)
    create_faiss_index(text_chunks)

    # Ask question
    user_question = st.text_input("Ask a question about your resume:")

    if user_question:
        with st.spinner("Analyzing resume..."):
            response = answer_question(user_question)
        st.markdown("### Answer:")
        st.write(response)

