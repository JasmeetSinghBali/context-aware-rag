import json
import logging

from app.retrieval.strategies import StrategyA, StrategyB

logger = logging.getLogger(__name__)


class BenchmarkService:
    def __init__(self, strategy_a: StrategyA, strategy_b: StrategyB):
        self.strategy_a = strategy_a
        self.strategy_b = strategy_b

    def _avg_distance(self, results):
        return sum(r["distance"] for r in results) / len(results)
    
    def _top_k_overlap(self, results_a, results_b):
        set_a = {r["text"] for r in results_a}
        set_b = {r["text"] for r in results_b}

        intersection = set_a.intersection(set_b)

        k = max(len(set_a), 1)

        return len(intersection) / k

    def run(self, queries: list[str]):
        report = []

        for q in queries:
            result_a = self.strategy_a.run(q)
            result_b = self.strategy_b.run(q)

            score_a = self._avg_distance(result_a["results"])
            score_b = self._avg_distance(result_b["results"])

            gain = score_a - score_b

            overlap = self._top_k_overlap(
                result_a["results"],
                result_b["results"]
            )

            report.append({
                "query": q,

                "strategy_a": {
                    "results": result_a["results"],
                    "avg_distance": score_a,
                },

                "strategy_b": {
                    "expanded_query": result_b["expanded_query"],
                    "results": result_b["results"],
                    "avg_distance": score_b,
                },

                "retrieval_gain": gain,
                "top_k_overlap": overlap
            })
        
        avg_gain = sum(r["retrieval_gain"] for r in report) / len(report)
        wins_b = sum(1 for r in report if r["retrieval_gain"] > 0)
        wins_a = sum(1 for r in report if r["retrieval_gain"] < 0)

        avg_overlap = sum(r["top_k_overlap"] for r in report) / len(report)

        summary = {
            "average_retrieval_gain": avg_gain,
            "average_top_k_overlap": avg_overlap,
            "strategy_b_wins": wins_b,
            "strategy_a_wins": wins_a,
            "total_queries": len(report)
        }

        return {
            "results": report,
            "summary": summary
        }

    def save_report(self, report, path="retrieval_benchmark.md"):
        with open(path, "w") as f:
            f.write("# Retrieval Benchmark Report\n\n")

            f.write("## Summary\n")
            f.write("```json\n")
            f.write(json.dumps(report["summary"], indent=2))
            f.write("\n```\n\n")

            f.write("## Detailed Results\n")
            f.write("```json\n")
            f.write(json.dumps(report["results"], indent=2))
            f.write("\n```")

        logger.info(f"Benchmark saved to {path}")