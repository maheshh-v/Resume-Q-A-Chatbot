import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_input):
    """
    Extract text from a PDF.
    pdf_input can be:
    - a file path (str), or
    - a Streamlit UploadedFile object
    """
    full_text = ""

    if isinstance(pdf_input, str):
        # Case 1: Local file path
        pdf_doc = fitz.open(pdf_input)
    else:
        # Case 2: Streamlit UploadedFile (in-memory)
        pdf_bytes = pdf_input.read()
        pdf_doc = fitz.open("pdf", pdf_bytes)

    for page in pdf_doc:
        full_text += page.get_text()

    pdf_doc.close()

    if not full_text.strip():
        raise ValueError("No text found in PDF")

    return full_text
