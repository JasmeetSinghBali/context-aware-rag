# Context Aware RAG

Local semantic retrieval RAG Stub and Mocks Vertex AI SDK TextEmbeddings and GenerativeModel.

- Strategy A — Raw Vector Search
- Strategy B — Query Expansion Retrieval


Tech Stack:
- FastAPI
- ChromaDB
- sentence-transformers
- uv

```bash
context-aware-rag/
│
├── app/
│   ├── api/
│   │   └── __init__.py
│   │   └── routes.py
│   │
│   ├── core/
│   │   └── __init__.py
│   │   ├── config.py
│   │   └── constants.py
│   │   └── logging.py
│   │
│   ├── embeddings/
│   │   └── __init__.py
│   │   └── mock_text_embedding.py
│   │
│   ├── generation/
│   │   └── __init__.py
│   │   └── mock_generational_model.py
│   │
│   ├── retrieval/
│   │   └── __init__.py
│   │   └── chroma_store.py
│   │   └── retriever.py
│   │   └── strategies.py
│   │
│   ├── ingestion/
│   │   └── __init__.py
│   │   └── chunker.py
│   │   └── ingest_service.py
|   |
│   ├── evaluation/
│   │   └── __init__.py
│   │   └── benchmark.py
|   |
│   |── __init__.py
│   └── main.py
│
├── data/
│   └── sample_documents.txt
│
├── reports/
│
├── tests/
│   ├── test_embeddings.py
│   ├── test_retrieval.py
│
├── debug_chromadb.py 
├── .env
├── README.md
├── DOCUMENTATION.md
└── pyproject.toml


# sync/install depend, venv creation and scaffold setup automatically
uv sync

# lint sanity check
uv run ruff check .

# local backend with chromadb local ./chroma_db persistance
uv run uvicorn app.main:app --reload

# sanity check chromadb collection, sim search query
uv run python debug_chromadb.py

# test
uv run pytest

```