import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """Extract text from uploaded PDF file."""
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

def fetch_job_description(jd_input):
    """Return clean job description text from input box."""
    return jd_input.strip()
