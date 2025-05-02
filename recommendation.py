from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load assessment data
with open("catalog_data.json", "r") as f:
    catalog = json.load(f)

# Prepare index
embeddings = np.array([model.encode(item["description"]) for item in catalog]).astype("float32")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def get_recommendations(query, top_k=10):
    query_vec = model.encode([query]).astype("float32")
    scores, indices = index.search(query_vec, top_k)
    return [catalog[i] for i in indices[0]]