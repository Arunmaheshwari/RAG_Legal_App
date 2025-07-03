# 🧠 RAG Chatbot for Legal Documents

A Retrieval-Augmented Generation (RAG) chatbot built using **LangChain**, **FAISS**, **Sentence Transformers**, and **Ollama** LLMs. Designed to help users query large legal documents with grounded, contextual answers.

---

## 📌 Features

- 🔍 **Contextual Retrieval**: Uses FAISS with semantic search for document chunking.
- 🧠 **Local LLMs**: Integrates `llama3`, `mistral`, or `tiny` via Ollama.
- 📄 **PDF Loader**: Parses and chunks legal PDFs into retrievable units.
- 💬 **Streamlit Chat Interface**: Easy-to-use front-end for user interaction.
- ⚙️ **Environment Config**: Uses `.env` for easy config of embedding model and DB path.

---

## 🧰 Tech Stack

| Tool                | Purpose                         |
|---------------------|---------------------------------|
| `Streamlit`         | Chat UI                         |
| `LangChain`         | RAG pipeline orchestration      |
| `FAISS`             | Vector database                 |
| `sentence-transformers` | Embedding model (`MiniLM`) |
| `Ollama`            | Local LLM backend               |
| `pypdf`             | PDF parsing                     |
| `python-dotenv`     | Environment variable loading    |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Arunmaheshwari/RAG_Legal_App.git
cd RAG_Legal_App or RAG_Application
