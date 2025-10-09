import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_input):
    full_text = ""

    if isinstance(pdf_input, str):
        pdf_doc = fitz.open(pdf_input)
    else:
        pdf_bytes = pdf_input.read()
        pdf_doc = fitz.open("pdf", pdf_bytes)

    for page in pdf_doc:
        full_text += page.get_text()

    pdf_doc.close()

    if not full_text.strip():
        raise ValueError("No text found in PDF")

    return full_text
