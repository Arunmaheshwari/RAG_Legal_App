import streamlit as st
from dotenv import load_dotenv
import os

from chunks.chunks import load_and_chunk_pdf
from vectordb.vectordf import create_or_load_vectorstore
from src.prompt_template import get_prompt_template
from src.retriever import setup_retriever
from src.ollama_llm import load_llm
from langchain_community.llms import Ollama

# Load environment
load_dotenv()
LLM_MODEL = os.getenv("LLM_MODEL")
EMBED_MODEL = os.getenv("EMBED_MODEL")
DB_PATH = os.getenv("DB_PATH")

# Streamlit setup
st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("🧠 RAG Chatbot for Legal Documents")

# Load and prepare data
retriever, num_chunks = setup_retriever()

# Sidebar info

st.sidebar.markdown(f"**Chunks Indexed**: `{num_chunks}`")
st.sidebar.markdown("**Embedding is Done by**: `Transformer Library`")
st.sidebar.markdown(f"**Embedding Model**: `{EMBED_MODEL}`")
st.sidebar.markdown("**LLM**: `Ollama`")
st.sidebar.markdown(f"**LLM Model**: `{LLM_MODEL}`")


# LLM & Prompt setup
llm = load_llm()
prompt_template = get_prompt_template()

# Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
with st.form("user_input_form", clear_on_submit=True):
    question = st.text_input("Ask a question:")
    submitted = st.form_submit_button("Submit")

if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Process query
if submitted and question:
    try:
        docs = retriever.invoke(question)
        context = "\n\n".join(doc.page_content for doc in docs)
        final_prompt = prompt_template.format(context=context, question=question)

        # Display user question
        st.chat_message("user").markdown(question)

        # Stream model response
        with st.chat_message("assistant"):
            response = ""
            message_placeholder = st.empty()
            for chunk in llm.stream(final_prompt):
                response += chunk
                message_placeholder.markdown(response + "▌")
            message_placeholder.markdown(response)

        # Save to history
        st.session_state.chat_history.append((question, response))

        # Show source docs
        with st.expander("📄 Source Chunks"):
            for i, doc in enumerate(docs):
                st.markdown(f"**Chunk {i+1}:**")
                st.code(doc.page_content.strip()[:1000])

    except Exception as e:
        st.error(f"Error: {e}")