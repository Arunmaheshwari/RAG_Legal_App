import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings(model_name: str):
    return HuggingFaceEmbeddings(model_name=model_name)

def create_or_load_vectorstore(docs, db_path, embed_model):
    embeddings = get_embeddings(embed_model)
    if os.path.exists(db_path):
        return FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
    else:
        db = FAISS.from_documents(docs, embeddings)
        db.save_local(db_path)
        return db
