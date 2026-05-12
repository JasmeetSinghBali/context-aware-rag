import logging

logger = logging.getLogger(__name__)


class MockGenerativeModel:
    """
    <mock stub>
    Vertex AI GenerativeModel for query expansion.
    No LLM used — deterministic rule-based expansion.
    """

    def expand_query(self, query: str) -> str:
        q = query.lower()
        expansions = []

        # SYSTEM SCALING INTENT
        if any(k in q for k in ["peak", "load", "traffic", "scale"]):
            expansions.append(
                "horizontal scaling autoscaling load balancing distributed systems concurrency traffic spikes"
            )

        # RELIABILITY INTENT
        if any(k in q for k in ["reliability", "stress", "failure", "resilience"]):
            expansions.append(
                "fault tolerance redundancy failover high availability system resilience"
            )

        # PERFORMANCE INTENT
        if any(k in q for k in ["latency", "fast", "performance"]):
            expansions.append(
                "caching optimization response time performance tuning edge computing"
            )

        expanded = f"{query} " + " ".join(expansions)

        logger.info(f"[Query Expansion] {expanded}")

        return expanded