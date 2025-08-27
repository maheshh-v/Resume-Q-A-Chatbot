
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_into_chunks(resume_text, chunk_size=800, chunk_overlap=80):
    # Split resume into smaller pieces for better search
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_text(resume_text)