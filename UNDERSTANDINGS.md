# Here is where i document my learning journey

1. Initially, Here is what my pipeline was working
    1. Get the PDF
    2. Chunk the PDF into the required size
    3. Once chunked, get the text content
    4. Parse each text content and convert them into embeddings

2. But this is a better method, and here is how it works
    1. Get the PDF
    2. Generate the Chunks
    3. Once, the text content is in reach
    4. Generate the text_list which is a list with all the content in the form of 1D list
    5. Once we have that list, we can directly pass this as payload to the embeddings model to parse them
    Why this is better?
        1. We are processing almost all of the text items(basically chunks) in a single network call.
        2. We can use this list as it is.

3. How We upsert the data?
    1. Byfar, this was the difficult thing, but with my understand, we can upsert `points` into the vectorDB
    2. Where each point is of the type of `qdrant_client.http.models.PointStruct` which has 3 parameters:
    `ID, payload, vector`
    3. The highlight is that, because we use VectorDB with RAG, we need to have the text_data along with the vector in the same point for easy semantic search. and that goes into the payload.
    4. The ID is preferably a UUID so that duplicate items can also be added.
    5. Finally, the vector is the direct embedding vector.
    6. Multiple points are stored into a single `points`variable and we can upsert this points directly into the collections.
