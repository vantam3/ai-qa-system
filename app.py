import streamlit as st
from utils.pdf_processor import extract_text_from_pdf
from utils.vector_store import create_embeddings, create_faiss_index, search_faiss
from utils.ai_model import generate_answer_huggingface

st.title("AI-powered Q&A System (Hugging Face)")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    pdf_path = f"data/{uploaded_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text_from_pdf(pdf_path)
    texts = text.split("\n\n")

    embeddings = create_embeddings(texts)
    faiss_index = create_faiss_index(embeddings)

    user_query = st.text_input("Ask a question:")
    if user_query:
        retrieved_texts = search_faiss(user_query, texts, faiss_index)
        context = "\n".join(retrieved_texts)
        response = generate_answer_huggingface(context, user_query)
        st.write(response)
