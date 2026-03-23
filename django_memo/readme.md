next steps:
docker exec -it ollama ollama pull llama3
docker exec -it ollama ollama pull nomic-embed-text

errors:

pulling 6a0746a1ec1a:  31% ▕█████████████████                                      ▏ 1.5 GB/4.7 GB
Error: max retries exceeded: Get "https://dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com/ollama/docker/registry/v2/blobs/sha256/6a/6a0746a1ec1aef3e7ec53868f220ff6e389f6f8ef87a01d77c96807de94ca2aa/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=66040c77ac1b787c3af820529859349a%2F20260309%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260309T023413Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a415a677b61557e57b216bdd6c0cb9f702c3cf2e989da9b5ff08ce3c0b424a12": dial tcp: lookup dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com on 127.0.0.11:53: no such host
pulling manifest
Error: pull model manifest: Get "https://registry.ollama.ai/v2/library/nomic-embed-text/manifests/latest": dial tcp: lookup registry.ollama.ai on 127.0.0.11:53: no such host
(.venv) PS E:\llm\AI_Agent\django_memo\app> 




------------------------------------- concepts-----------------------------
.............Quadrant....................
quandrant is primarly high performance vector database used by Mem0 for stroing and searching long-term user memories.

 Qdrant supports the "Vector Store" component in Mem0's hybrid architecture (which also uses relational databases like SQLite or Postgres for metadata)

 note:
memory history → Django DB
vector memory → Qdrant
embeddings → Ollama
LLM → Ollama


............................... qdrant and nomic-embed-text ...............................
How they work together in Semantic Search .
- Generation: You use a model like nomic-embed-text to turn your documents into vectors.
- Storage: You upload these vectors to Qdrant.
Search: When a user types a query, you turn that query into a vector too.
- Retrieval: Qdrant compares the query vector to all stored vectors using mathematical distance (like Cosine Similarity) to find the ones that are "closest" in meaning.

note: for similarity search we need same lenght vectors
 otherwise you will get error:
 ValueError: shapes (0,1536) and (768,) not aligned

 here stoarge it means qdrant is 1536 dimension, but nomic-embed-text is 768 dimension
 