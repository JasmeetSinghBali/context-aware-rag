from app.retrieval.retriever import Retriever
from app.generation.mock_generational_model import MockGenerativeModel


class StrategyA:
    """
    Raw embedding-based retrieval (baseline)
    """

    def __init__(self, retriever: Retriever):
        self.retriever = retriever

    def run(self, query: str, top_k: int = 3):
        return {
            "query": query,
            "results": self.retriever.retrieve(query, top_k=top_k)
        }
    


class StrategyB:
    """
    Query expansion + retrieval strategy (AI-enhanced mock)
    """

    def __init__(self, retriever):
        self.retriever = retriever
        self.generator = MockGenerativeModel()

    def run(self, query: str, top_k: int = 3):
        expanded_query = self.generator.expand_query(query)

        return {
            "original_query": query,
            "expanded_query": expanded_query,
            "results": self.retriever.retrieve(expanded_query, top_k=top_k),
        }