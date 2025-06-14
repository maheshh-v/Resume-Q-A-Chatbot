import streamlit as st
from utils.extract_text import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.embed_store import create_faiss_index
from utils.qa_chain import answer_question
import os

st.set_page_config(page_title="Smart Resume Q&A", layout="centered")

st.title("📄 Smart Resume Q&A Chatbot")
st.write("Upload your resume and ask questions about it!")

# Upload section
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file:
    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Resume uploaded and processed!")

    # Extract and embed
    text = extract_text_from_pdf("resume.pdf")
    chunks = split_text_into_chunks(text)
    create_faiss_index(chunks)

    # Ask question
    query = st.text_input("Ask a question about your resume:")

    if query:
        with st.spinner("Searching and thinking..."):
            answer = answer_question(query)
        st.markdown("### 🧠 Answer:")
        st.write(answer)
