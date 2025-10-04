import streamlit as st
from utils.text_extraction import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.qa_chain import answer_question, perform_recruiter_search
from utils.data_ingestion import embed_and_upsert_chunks
import uuid
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Resume Analyzer", layout="wide", initial_sidebar_state="expanded")

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]

if 'uploaded_files_list' not in st.session_state:
    st.session_state.uploaded_files_list = []

user_namespace = st.session_state.session_id

def build_search_ui():
    # TODO: add export results feature
    tab1, tab2 = st.tabs(["Search All Resumes", "Single Resume Q&A"])
    
    with tab1:
        st.header("Search All Resumes")
        st.write("Enter job requirements to find matching candidates from your uploaded resumes.")
        
        recruiter_query = st.text_area(
            "Job Requirements:", 
            placeholder="Python developer with 3+ years experience in machine learning",
            height=200
        )
        
        if st.button("Analyze Candidates", type="primary"):
            if recruiter_query:
                with st.spinner("Searching..."):
                    response = perform_recruiter_search(recruiter_query, user_namespace)
                st.markdown("### Results:")
                st.write(response)
            else:
                st.warning("Please enter your job requirements.")
    
    with tab2:
        st.header("Ask Questions About a Specific Resume")
        st.write("Select a resume and ask detailed questions about that candidate.")
        
        available_resumes = st.session_state.get("uploaded_files_list", [])
        
        if available_resumes:
            selected_resume = st.selectbox("Choose resume:", available_resumes)
            
            user_question = st.text_input(
                "Your question:",
                placeholder="What programming languages does this candidate know?"
            )
            
            if user_question:
                with st.spinner("Loading..."):
                    response = answer_question(user_question, selected_resume=selected_resume, namespace=user_namespace)
                st.markdown("### Answer:")
                st.write(response)
        else:
            st.warning("No resumes available. Please upload resumes first.")

st.sidebar.title("Upload Resumes")
st.sidebar.caption(f"Session: {st.session_state.session_id}")

uploaded_files = st.sidebar.file_uploader(
    "Choose PDF files:", 
    type="pdf", 
    accept_multiple_files=True,
    help="Upload resume PDFs to search and analyze",
    key="file_uploader"
)

if uploaded_files:
    with st.sidebar:
        for uploaded_file in uploaded_files:
            filename = uploaded_file.name
            file_size_mb = uploaded_file.size / (1024 * 1024)
            
            if file_size_mb > 10:
                st.error(f"❌ {filename}: File too large ({file_size_mb:.1f}MB). Max 10MB allowed.")
                continue
            
            if filename not in st.session_state.uploaded_files_list:
                try:
                    with st.spinner(f"Processing {filename}..."):
                        resume_text = extract_text_from_pdf(uploaded_file)
                        text_chunks = split_text_into_chunks(resume_text)
                        embed_and_upsert_chunks(text_chunks, filename, user_namespace)
                    
                    st.session_state.uploaded_files_list.append(filename)
                    st.success(f"✅ {filename} ready")
                except Exception as e:
                    st.error(f"❌ {filename}: Could not process file")
                    print(f"Error: {e}")

if st.session_state.uploaded_files_list:
    st.sidebar.markdown("---")
    st.sidebar.subheader(f"Uploaded Files ({len(st.session_state.uploaded_files_list)})")
    
    for idx, file in enumerate(st.session_state.uploaded_files_list):
        col1, col2 = st.sidebar.columns([3, 1])
        with col1:
            st.write(f"{file}")
        with col2:
            if st.button("🗑️", key=f"delete_{idx}", help=f"Delete {file}"):
                st.session_state.uploaded_files_list.remove(file)
                st.rerun()
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Clear All & Start Fresh", type="secondary", use_container_width=True):
        st.session_state.clear()
        st.rerun()

st.title("Resume Analyzer")
st.markdown("*Search resumes and analyze candidates*")

if not st.session_state.uploaded_files_list:
    st.info("**Get Started:** Upload resumes using the sidebar to begin searching")
else:
    build_search_ui()