from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_into_chunks(text, chunk_size=800, chunk_overlap=80):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

from utils.extract_text import extract_text_from_pdf
#
# text = extract_text_from_pdf("../resume.pdf")
# chunks = split_text_into_chunks(text)
# print(chunks[:2])  # Show first 2 chunks