import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load mô hình tạo vector embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(texts):
    """Tạo embeddings từ danh sách văn bản"""
    return model.encode(texts)

def create_faiss_index(embeddings):
    """Tạo FAISS index"""
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(np.array(embeddings))
    return index

def search_faiss(query, texts, index, top_k=3):
    """Tìm kiếm văn bản phù hợp nhất từ FAISS"""
    query_embedding = model.encode([query])
    _, I = index.search(query_embedding, top_k)
    return [texts[i] for i in I[0]]
