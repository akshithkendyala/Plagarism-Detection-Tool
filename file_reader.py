import PyPDF2
from docx import Document

def extract_text(file):

    filename = file.filename.lower()

    if filename.endswith('.txt'):
        return file.read().decode('utf-8')

    elif filename.endswith('.pdf'):
        text = ""

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

        return text

    elif filename.endswith('.docx'):

        doc = Document(file)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    return ""