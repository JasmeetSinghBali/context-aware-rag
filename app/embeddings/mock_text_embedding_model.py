from sentence_transformers import SentenceTransformer
import numpy as np
from app.core.constants import EMBEDDING_MODEL_NAME

class MockEmbedding:
    def __init__(self, values: list[float]):
        self.values = values


class MockTextEmbeddingModel:
    """
    <mock stub>
    vertexai.language_models.TextEmbeddingModel
    """

    _instance = None

    def __init__(self, model_name: str = EMBEDDING_MODEL_NAME):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    @classmethod
    def from_pretrained(cls, model_name: str):
        if cls._instance is None:
            cls._instance = cls(model_name)
        return cls._instance

    def get_embeddings(self, texts: list[str]) -> list[MockEmbedding]:
        vectors = self.model.encode(texts)

        # normalize to magnitude of 1 vector representation for faster cosine similarity via dot product b/w two vectors
        vectors = np.array(vectors)
        vectors = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)

        # example- [MockEmbedding([0.6, 0.8]), MockEmbedding([0.0, 1.0])]
        return [MockEmbedding(v.tolist()) for v in vectors]