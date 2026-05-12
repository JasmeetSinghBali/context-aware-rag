import chromadb
# from chromadb.config import Settings as ChromaSettings
import logging

logger = logging.getLogger(__name__)

class ChromaStore:
    """
    Abstraction over ChromaDB for vector storage + retrieval.
    """

    def __init__(self, collection_name: str = "rag_chunks"):
        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(
        self,
        ids: list[str],
        embeddings: list[list[float]],
        documents: list[str],
        metadatas: list[dict],
    ):
        logger.info(f"Adding {len(ids)} documents to ChromaDB")
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def query(self, query_embedding: list[float], top_k: int = 3):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas", "distances"]
        )