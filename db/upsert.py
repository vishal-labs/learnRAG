from qdrant_client import QdrantClient
from qdrant_client.http import models
import uuid
from embeddings import embeddings as emb

client = QdrantClient(url="http://localhost:6333")


def upsert_embeddings(collection_name: str, embeddings_list, texts_list):

    if not client.collection_exists(collection_name=collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=768, distance=models.Distance.COSINE
            ),
        )

    try:
        points = []
        for i, embed in enumerate(embeddings_list):
            point = models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embed,
                payload={"text_str": texts_list[i], "chunk_id": i},
            )
            points.append(point)
        client.upsert(collection_name=collection_name, points=points)
    except Exception as e:
        print(f"Error inserting vectors: {e}")


def query_collection(collection_name, query_text, limit=5):
    try:
        query_embedding = emb.embed_query(query_text)

        search_result = client.query_points(
            collection_name=collection_name,
            query=query_embedding,
            limit=limit,
        )

        return search_result.points

    except Exception as e:
        print(f"Error querying collection: {e}")
        return []


def delete_collection(collection_name):
    if client.collection_exists(collection_name):
        client.delete_collection(collection_name)
        return f"Collection {collection_name} deleted"
    else:
        return "Collection Doesn't Exist"
