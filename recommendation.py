from sentence_transformers import SentenceTransformer
import faiss
import json

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load assessment data
with open("catalog_data.json", "r") as f:
    catalog = json.load(f)

# Prepare index
embeddings = [model.encode(item["description"]) for item in catalog]
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)

def get_recommendations(query, top_k=10):
    query_vec = model.encode([query])
    scores, indices = index.search(query_vec, top_k)
    return [catalog[i] for i in indices[0]]