import uuid
import logging

from app.ingestion.chunker import Chunker
from app.retrieval.chroma_store import ChromaStore
from app.embeddings.mock_text_embedding_model import MockTextEmbeddingModel


logger = logging.getLogger(__name__)


class IngestionService:
    def __init__(
        self,
        store: ChromaStore,
        embedding_model: MockTextEmbeddingModel,
    ):
        self.store = store
        self.embedding_model = embedding_model
        self.chunker = Chunker()

    def ingest(self, text: str, source: str = "manual_input"):
        logger.info("Starting ingestion pipeline")

        chunks = self.chunker.chunk_text(text)
        logger.info(f"Created {len(chunks)} chunks")

        embeddings = self.embedding_model.get_embeddings(chunks)

        ids = [str(uuid.uuid4()) for _ in chunks]

        metadatas = [
            {
                "source": source,
                "chunk_index": i
            }
            for i in range(len(chunks))
        ]

        self.store.add_documents(
            ids=ids,
            embeddings=[e.values for e in embeddings],
            documents=chunks,
            metadatas=metadatas,
        )

        logger.info("Ingestion completed successfully")

        return {
            "chunks_ingested": len(chunks),
            "source": source
        }