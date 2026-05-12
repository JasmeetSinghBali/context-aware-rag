from app.retrieval.chroma_store import ChromaStore
from app.retrieval.retriever import Retriever
from app.embeddings.mock_text_embedding_model import MockTextEmbeddingModel


def test_retrieval_smoke():
    embedder = MockTextEmbeddingModel.from_pretrained("all-MiniLM-L6-v2")
    store = ChromaStore()

    retriever = Retriever(store, embedder)

    # minimal fake ingestion
    docs = ["System scales using load balancers"]
    embs = embedder.get_embeddings(docs)

    store.add_documents(
        ids=["1"],
        embeddings=[emb.values for emb in embs],
        documents=docs,
        metadatas=[{"source": "test"}]
    )

    result = retriever.retrieve("How does scaling work?")

    assert len(result) > 0