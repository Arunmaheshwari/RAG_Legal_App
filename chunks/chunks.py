from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader

def load_and_chunk_pdf(file_path: str):
    reader = PdfReader(file_path)
    raw_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            raw_text += text + "\n"

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    return splitter.create_documents([raw_text])