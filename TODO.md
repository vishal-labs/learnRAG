- [x] Implement a PDF ingestion pipeline
- [x] Insert Data into Qdrant localDB
- [x] Understand and implement client.Query part for the DB
- [x] Implement a RAG chain for question answering
- [x] Use ChatPromptTemplate and chain syntax
- [x] Format context properly before passing to LLM

## Next Steps

### Immediate (Easy Wins)

- [ ] Add source citations (page numbers, chunk IDs) to answers
- [ ] Move hardcoded PDF path to a constant
- [ ] Add support for multiple PDFs in a single collection
- [ ] Add basic logging instead of print statements

### Medium (Better Quality)

- [ ] Implement re-ranking of retrieved chunks
- [ ] Add query expansion for better retrieval
- [ ] Try semantic chunking instead of fixed-size chunking
- [ ] Add conversation memory for multi-turn chats
- [ ] Add retry logic and timeouts for API calls

### Advanced (Production Ready)

- [ ] Build a web UI (Streamlit/FastAPI)
- [ ] Add evaluation metrics (RAGAS or similar)
- [ ] Implement hybrid search (BM25 + vector)
- [ ] Add document metadata filtering (date, source, etc.)
- [ ] Switch to LangChain's built-in RAG utilities (create_retrieval_chain)

