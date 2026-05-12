# Retrieval Benchmark Report

## Summary
```json
{
  "average_retrieval_gain": 0.0225720869170295,
  "average_top_k_overlap": 0.7777777777777778,
  "strategy_b_wins": 2,
  "strategy_a_wins": 0,
  "total_queries": 3
}
```

## Detailed Results
```json
[
  {
    "query": "How does the system handle peak load?",
    "strategy_a": {
      "results": [
        {
          "text": "System handles peak load using autoscaling and load balancing.",
          "metadata": {
            "chunk_index": 0,
            "source": "api"
          },
          "distance": 0.1965767741203308
        },
        {
          "text": "The system handles peak load using horizontal scaling and load balancing across multiple instances.",
          "metadata": {
            "chunk_index": 0,
            "source": "sample_documents.txt"
          },
          "distance": 0.30644214153289795
        },
        {
          "text": "System scales using load balancers",
          "metadata": {
            "source": "test"
          },
          "distance": 0.4083212614059448
        }
      ],
      "avg_distance": 0.30378005901972455
    },
    "strategy_b": {
      "expanded_query": "How does the system handle peak load? horizontal scaling autoscaling load balancing distributed systems concurrency traffic spikes",
      "results": [
        {
          "text": "System handles peak load using autoscaling and load balancing.",
          "metadata": {
            "source": "api",
            "chunk_index": 0
          },
          "distance": 0.18352985382080078
        },
        {
          "text": "The system handles peak load using horizontal scaling and load balancing across multiple instances.",
          "metadata": {
            "source": "sample_documents.txt",
            "chunk_index": 0
          },
          "distance": 0.2211754322052002
        },
        {
          "text": "System scales using load balancers",
          "metadata": {
            "source": "test"
          },
          "distance": 0.3545365333557129
        }
      ],
      "avg_distance": 0.2530806064605713
    },
    "retrieval_gain": 0.05069945255915326,
    "top_k_overlap": 1.0
  },
  {
    "query": "How does scaling work in distributed systems?",
    "strategy_a": {
      "results": [
        {
          "text": "System scales using load balancers",
          "metadata": {
            "source": "test"
          },
          "distance": 0.3980426788330078
        },
        {
          "text": "The system handles peak load using horizontal scaling and load balancing across multiple instances.",
          "metadata": {
            "source": "sample_documents.txt",
            "chunk_index": 0
          },
          "distance": 0.4537653923034668
        },
        {
          "text": "System handles peak load using autoscaling and load balancing.",
          "metadata": {
            "source": "api",
            "chunk_index": 0
          },
          "distance": 0.4862404465675354
        }
      ],
      "avg_distance": 0.44601617256800336
    },
    "strategy_b": {
      "expanded_query": "How does scaling work in distributed systems? ",
      "results": [
        {
          "text": "System scales using load balancers",
          "metadata": {
            "source": "test"
          },
          "distance": 0.3980426788330078
        },
        {
          "text": "The system handles peak load using horizontal scaling and load balancing across multiple instances.",
          "metadata": {
            "chunk_index": 0,
            "source": "sample_documents.txt"
          },
          "distance": 0.4537653923034668
        },
        {
          "text": "System handles peak load using autoscaling and load balancing.",
          "metadata": {
            "chunk_index": 0,
            "source": "api"
          },
          "distance": 0.4862404465675354
        }
      ],
      "avg_distance": 0.44601617256800336
    },
    "retrieval_gain": 0.0,
    "top_k_overlap": 1.0
  },
  {
    "query": "What ensures system reliability under stress?",
    "strategy_a": {
      "results": [
        {
          "text": "Backpressure handling ensures system stability during overload conditions.",
          "metadata": {
            "chunk_index": 14,
            "source": "sample_documents.txt"
          },
          "distance": 0.3668067455291748
        },
        {
          "text": "Observability tools help monitor system performance under stress.",
          "metadata": {
            "chunk_index": 10,
            "source": "sample_documents.txt"
          },
          "distance": 0.3933371305465698
        },
        {
          "text": "Retry mechanisms improve reliability in transient failure scenarios.",
          "metadata": {
            "chunk_index": 13,
            "source": "sample_documents.txt"
          },
          "distance": 0.39740419387817383
        }
      ],
      "avg_distance": 0.38584935665130615
    },
    "strategy_b": {
      "expanded_query": "What ensures system reliability under stress? fault tolerance redundancy failover high availability system resilience",
      "results": [
        {
          "text": "Fault tolerance is achieved through redundancy, failover systems, and distributed deployment.",
          "metadata": {
            "source": "sample_documents.txt",
            "chunk_index": 2
          },
          "distance": 0.24143469333648682
        },
        {
          "text": "Retry mechanisms improve reliability in transient failure scenarios.",
          "metadata": {
            "chunk_index": 13,
            "source": "sample_documents.txt"
          },
          "distance": 0.3616030216217041
        },
        {
          "text": "Distributed databases replicate data across regions for high availability.",
          "metadata": {
            "source": "sample_documents.txt",
            "chunk_index": 7
          },
          "distance": 0.5034599304199219
        }
      ],
      "avg_distance": 0.3688325484593709
    },
    "retrieval_gain": 0.01701680819193524,
    "top_k_overlap": 0.3333333333333333
  }
]
```