import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(texts):
    return model.encode(texts)

def create_faiss_index(embeddings):
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(np.array(embeddings))
    return index

def search_faiss(query, texts, index, top_k=3):
    query_embedding = model.encode([query])
    _, I = index.search(query_embedding, top_k)
    return [texts[i] for i in I[0]]
