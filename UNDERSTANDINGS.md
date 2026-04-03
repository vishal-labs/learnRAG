# Here is where I document my learning journey

## 1. Initial Pipeline

My first pipeline worked like this:

1. Get the PDF
2. Chunk the PDF into the required size
3. Once chunked, get the text content
4. Parse each text content and convert them into embeddings

## 2. Improved Pipeline (Batch Embeddings)

A better method, and here is how it works:

1. Get the PDF
2. Generate the chunks
3. Once the text content is in reach, generate `text_list` — a 1D list with all the content
4. Pass this list directly as payload to the embeddings model

**Why this is better:**

- We are processing almost all of the text items (basically chunks) in a single network call
- We can use this list as it is

## 3. How We Upsert the Data

This was the difficult part, but here is my understanding:

- We upsert `points` into the vector DB
- Each point is of type `qdrant_client.http.models.PointStruct` which has 3 parameters:
  - `id` — preferably a UUID so that duplicate items can also be added
  - `payload` — the text data along with metadata (needed for semantic search + context retrieval)
  - `vector` — the direct embedding vector
- Multiple points are stored in a single `points` variable and we can upsert them directly into the collections

## 4. Prompt Templates and Chain Syntax

- Instead of manually formatting prompts with f-strings, we use `ChatPromptTemplate` from `langchain_core.prompts`
- The template has variables like `{context}` and `{question}` which we fill at runtime
- We can create a chain using the pipe operator: `chain = prompt | model`
- This chain is created once at module level, not on every function call, which is more efficient
- Invoking the chain is just `chain.invoke({"context": context_text, "question": query})`
- `model.invoke` returns an `AIMessage` object, and we access the actual text via `.content`

## 5. Context Formatting for the LLM

- `query_collection` returns points, and each point has a `.payload` which is a dict
- We extract only the `text_str` from each payload, not the entire dict
- We join all context texts with a separator like `---` to make it readable for the LLM
- If no context is found, we handle it gracefully instead of passing empty data

## 6. Constants and Configuration

- Hardcoded values like collection names should be defined as constants at the top
- This makes it easier to change them in one place instead of searching through files
