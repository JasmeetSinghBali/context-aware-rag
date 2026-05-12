"""
uv run python debug_chroma.py
"""
from app.retrieval.chroma_store import ChromaStore

store = ChromaStore()

res_collection_debug = store.collection.get(
    include=["documents", "metadatas"]
)

res_similarity_debug = store.query(
    query_embedding=[0.1] * 384,
    top_k=3
)

print(res_collection_debug)
print(res_similarity_debug)