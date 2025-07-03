import os
from chunks.chunks import load_and_chunk_pdf
from vectordb.vectordf import create_or_load_vectorstore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import streamlit as st

# Load environment
load_dotenv()
EMBED_MODEL = os.getenv("EMBED_MODEL")
DB_PATH = os.getenv("DB_PATH")


@st.cache_resource
def setup_retriever(file_path="data/AI Training Document.pdf"):
    docs = load_and_chunk_pdf(file_path)
    vectordb = create_or_load_vectorstore(docs, DB_PATH, EMBED_MODEL)
    retriever = vectordb.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "fetch_k": 20}
    )
    return retriever, len(docs)