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
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```


### 3. Configure Environment

Create a .env file with:

```bash
EMBED_MODEL=BAAI/bge-small-en
DB_PATH=vectordb/faiss_index
LLM_MODEL = tinyllama:latest
```
💡 You can also use other models like llama3, mistral, etc., by updating the LLM_MODEL in the .env.


### 4. Start Ollama & Pull Model
```bash
ollama pull tinyllama or tinyllama:latest
ollama run tinyllama or tinyllama:latest

```


### 5. Run the App
```bash
streamlit run app.py
```


# 📁 Project Structure

📦 Rag Legal document chatbot
├── app.py
├── .env
├── requirements.txt
├── chunks/
│   └── chunks.py
├── vectordb/
│   └── vectordf.py
├── src/
│   ├── ollama_llm.py
│   ├── prompt_template.py
│   └── retriever.py
└── data/
    └── AI Training Document.pdf


---

# 🔁 Project Workflow
flowchart TD

    A[📥 Ingestion Phase] --> A1[📄 Load PDF via PyPDF]
    A1 --> A2[✂️ Chunk Text using LangChain]
    A2 --> A3[🧠 Generate Embeddings (MiniLM)]
    A3 --> A4[💾 Store Chunks + Vectors in FAISS DB]

    B[📎 Augmentation Phase] --> B1[🔍 User Query Input (via Streamlit)]
    B1 --> B2[🔎 Retrieve Relevant Chunks from FAISS]
    B2 --> B3[📚 Merge Context with User Query]

    C[🤖 Generation Phase] --> C1[🧠 Pass Merged Context to Ollama LLM]
    C1 --> C2[💬 Generate Response]
    C2 --> C3[📤 Stream Output in Chat UI]

    A --> B
    B --> C


# 🔍 Stages Explained
 - Ingestion: Load PDFs → Chunk → Embed → Store in FAISS.

 - Augmentation: Take user query → Retrieve relevant chunks.

 - Generation: Combine context + query → Run through LLM → Generate answer.

---



# ✍️ Author
Arun Maheshwari