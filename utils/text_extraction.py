
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    full_text = ""
    with fitz.open(pdf_path) as pdf_doc:
        for page in pdf_doc:
            full_text += page.get_text()
    
    if not full_text.strip():
        raise ValueError("No text found in PDF")
    
    return full_text
