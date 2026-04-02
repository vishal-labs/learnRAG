from qdrant_client import QdrantClient
from qdrant_client.http import models
import uuid


# connecting to the client
client = QdrantClient(url="http://localhost:6333")


def upsert_embeddings(collection_name: str, embeddings_list, texts_list=None):

    if not client.collection_exists(collection_name=collection_name):
        # Creating a test collection, which loosely related to being a table in SQL
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=768, distance=models.Distance.COSINE
            ),
        )

    # Insert the actual vector points
    try:
        points = []
        for i, embed in enumerate(embeddings_list):
            point = models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embed,
                payload={"text_str": texts_list[i], "chunk_id": i}
            )
            points.append(point)
        client.upsert(collection_name=collection_name, points=points)
    except Exception as e:
        print(f"Error inserting vectors: {e}")


def query_collection(collection_name, query_text, limit=5):
    try:
        from create_embeddings import generate_embeddings
        # Generate embedding for the query text
        query_embedding = generate_embeddings(query_text)

        # Search for similar vectors
        search_result = client.search(
            collection_name=collection_name,
            query_vector=query_embedding[0].tolist()
            if hasattr(query_embedding[0], "tolist")
            else query_embedding[0],
            limit=limit,
        )
        return search_result
    except Exception as e:
        print(f"Error querying collection: {e}")
        return []


def delete_collection(collection_name):
    if client.collection_exists(collection_name):
        client.delete_collection(collection_name)
        return f"Collection {collection_name} deleted"
    else:
        return "Collection Doesn't Exist"
