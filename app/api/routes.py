from fastapi import File, UploadFile, Form, APIRouter
from typing import Optional
from pydantic import BaseModel

from app.ingestion.ingest_service import IngestionService
from app.embeddings.mock_text_embedding_model import MockTextEmbeddingModel

from app.retrieval.retriever import Retriever
from app.retrieval.strategies import StrategyA, StrategyB
from app.retrieval.chroma_store import ChromaStore

from app.evaluation.benchmark import BenchmarkService
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

class IngestRequest(BaseModel):
    text: str
    source: str = "api"

@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "context-aware-rag",
    }

@router.post("/ingest")
async def ingest_data(
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
):
    store = ChromaStore()
    embedder = MockTextEmbeddingModel.from_pretrained("all-MiniLM-L6-v2")

    service = IngestionService(store, embedder)

    # CASE 1: FILE INGESTION
    if file is not None:
        content = await file.read()
        decoded_text = content.decode("utf-8")

        logger.info(f"Ingesting file: {file.filename} with size {len(decoded_text)} chars")

        result = service.ingest(
            decoded_text,
            source=file.filename
        )

        return {
            "mode": "file",
            "filename": file.filename,
            **result
        }

    # CASE 2: TEXT INGESTION
    if text is not None:
        result = service.ingest(text, source="api_text")

        return {
            "mode": "text",
            **result
        }

    return {
        "error": "Provide either text or file"
    }

@router.post("/benchmark")
def benchmark():
    store = ChromaStore()
    embedder = MockTextEmbeddingModel.from_pretrained("all-MiniLM-L6-v2")
    retriever = Retriever(store, embedder)

    strategy_a = StrategyA(retriever)
    strategy_b = StrategyB(retriever)

    benchmark_service = BenchmarkService(strategy_a, strategy_b)

    queries = [
        "How does the system handle peak load?",
        "How does scaling work in distributed systems?",
        "What ensures system reliability under stress?"
    ]

    report = benchmark_service.run(queries)
    benchmark_service.save_report(report)

    return report