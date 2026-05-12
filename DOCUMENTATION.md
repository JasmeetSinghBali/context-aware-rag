```text
/ingest
    ↓
MockTextEmbeddingModel
    ↓
sentence-transformers
    ↓
ChromaDB


/benchmark
    ↓
Strategy A
    raw query
    ↓
    embedding
    ↓
    cosine search


Strategy B
    query
    ↓
MockGenerativeModel
(rule-based expansion)
    ↓
expanded query
    ↓
embedding
    ↓
cosine search
```

# 📊 Benchmark Evaluation Guide (Retrieval Metrics)


This project evaluates Retrieval-Augmented Generation (RAG) using two retrieval strategies:

* **Strategy A: Raw Vector Search**
* **Strategy B: Query-Expanded Vector Search (Mocked LLM rewrite)**

Each query is evaluated using multiple retrieval metrics to measure not just accuracy, but also retrieval behavior and stability.

---

## 🧪 Evaluation Metrics

### 1. Average Distance (`avg_distance`)

Measures how semantically close retrieved chunks are to the query.

* Computed using embedding distance (cosine-based similarity internally via sentence-transformers)
* Lower value = better semantic match

```text
avg_distance = mean(distance of top-k retrieved documents)
```

---

### 2. Retrieval Gain (`retrieval_gain`)

Measures improvement of Strategy B over Strategy A.

```text
retrieval_gain = avg_distance_A - avg_distance_B
```

### Interpretation:

| Value | Meaning                            |
| ----- | ---------------------------------- |
| > 0   | Query expansion improved retrieval |
| = 0   | No meaningful change               |
| < 0   | Query expansion degraded retrieval |

---

### 3. Top-K Overlap (`top_k_overlap`)

Measures how much retrieved content overlaps between Strategy A and Strategy B.

```text
overlap = |A ∩ B| / K
```

### Interpretation:

| Value | Meaning                                |
| ----- | -------------------------------------- |
| 1.0   | Identical retrieval results            |
| 0.5   | Partial shift in retrieval space       |
| 0.0   | Completely different retrieval results |

---

# 📐 Similarity Metric Choice: Cosine vs Euclidean

This project uses **cosine similarity (via sentence-transformers embeddings)**.

---

## 🧠 Why Cosine Similarity?

Cosine similarity measures:

> Orientation between vectors, not magnitude.

```text
cosine_similarity(A, B) = (A · B) / (||A|| ||B||)
```

### Why it fits RAG:

* Embeddings encode **semantic meaning as direction**
* Sentence length should NOT affect similarity
* Works well for normalized transformer embeddings

---

## ⚖️ Cosine vs Euclidean

| Metric             | Behavior        | Suitability for RAG          |
| ------------------ | --------------- | ---------------------------- |
| Cosine similarity  | Angle-based     | ✅ Best choice                |
| Euclidean distance | Magnitude-based | ⚠️ Sensitive to vector scale |

---

## 🚫 Why not Euclidean?

Euclidean distance:

```text
||A - B||
```

Problems:

* Sensitive to vector magnitude
* Poor performance in high-dimensional embedding spaces
* Less stable for sentence-transformer models

---

## ✅ Conclusion

> Cosine similarity is preferred for semantic retrieval systems using transformer embeddings.

---

# 🚀 Production Migration: Vertex AI Vector Search (Matching Engine)

This project currently uses:

* Sentence Transformers (`all-MiniLM-L6-v2`)
* ChromaDB (local vector store)
* Mocked Vertex AI interfaces

In production, this can be migrated to:

👉 **Vertex AI Vector Search (Matching Engine)**
Google Cloud Vertex AI

---

## 🧩 Current Architecture Mapping

| Local Component      | Vertex AI Equivalent                           |
| -------------------- | ---------------------------------------------- |
| SentenceTransformer  | Vertex Embedding Model (`textembedding-gecko`) |
| ChromaDB             | Vertex Vector Search Index                     |
| Cosine similarity    | ANN similarity in Matching Engine              |
| Mock GenerativeModel | Vertex LLM (Gemini / text-bison)               |

---

# 🔧 What changes in this repo

## 1. Embedding Layer

### File to change:

```
app/embeddings/text_embedding.py
```

### Replace:

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

### With:

```python
vertexai.language_models.TextEmbeddingModel
```

### Impact:

* Remove local HF dependency
* Replace `.encode()` with `.get_embeddings()`

---

## 2. Vector Store Layer

### File to change:

```
app/retrieval/chroma_store.py
```

### Replace ChromaDB with:

* Vertex AI Matching Engine index

### New responsibilities:

* Upsert vectors to Vertex Index
* Query nearest neighbors via Vertex API

---

## 3. Retrieval Layer

### File to change:

```
app/retrieval/strategies.py
```

### Strategy A changes:

```python
self.vectorstore.query(embedding)
```

➡ becomes:

```python
matching_engine.find_neighbors(vector)
```

---

## 4. Query Expansion Layer (Strategy B)

### File:

```
app/generation/mock_generational_model.py
```

### Replace mock:

```python
class MockGenerativeModel:
```

➡ with:

```python
vertexai.generative_models.GenerativeModel
```

---

## 5. Benchmark Layer 

### File:

```
app/evaluation/benchmark.py
```

changes:

* Custom tracing and instrumentation with opentelemetry for latency , time 
* Optional cost estimation (Vertex API calls)
* ragas or openevals or custom setup to modify report and evaluate on other parameters for relevancy, intent classification, hallucinations(wud need ground truth knowledge base reff as vectors, knowledge graphs or even simple llmwiki style .md files) etc..

---

## 📦 Deployment Evolution Path Could look like this

### Phase 1 (Current)

* Sentence Transformers
* ChromaDB
* Mock LLM with real LLM api external or local inference

### Phase 2

* Replace embeddings with Vertex AI embeddings
* Keep ChromaDB

### Phase 3

* Replace ChromaDB with Vertex Matching Engine
* Use real ANN search at scale

...so on