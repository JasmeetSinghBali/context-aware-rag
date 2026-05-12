from app.embeddings.mock_text_embedding_model import MockTextEmbeddingModel
from app.core.constants import EMBEDDING_MODEL_NAME

def test_embedding_shape():
    model = MockTextEmbeddingModel.from_pretrained(EMBEDDING_MODEL_NAME)

    embeddings = model.get_embeddings([
        "How does peak load handling work?"
    ])

    assert len(embeddings) == 1
    assert len(embeddings[0].values) > 100  # MiniLM ~384 dims default