from app.retrieval.chroma_store import ChromaStore
from app.embeddings.mock_text_embedding_model import MockTextEmbeddingModel
import logging

logger = logging.getLogger(__name__)

class Retriever:
    def __init__(self, store: ChromaStore, embedding_model: MockTextEmbeddingModel):
        self.store = store
        self.embedding_model = embedding_model

    def retrieve(self, query: str, top_k: int = 3):
        logger.info(f"Retrieving for query: {query}")
        embedding = self.embedding_model.get_embeddings([query])[0].values

        logger.info("Generated query embedding")

        results = self.store.query(
            query_embedding=embedding,
            top_k=top_k
        )

        logger.info(f"Retrieved {len(results['documents'][0])} documents")

        return self._format_results(results)

    def _format_results(self, results):
        return [
            {
                "text": doc,
                "metadata": meta,
                "distance": dist,
            }
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0],
            )
        ]