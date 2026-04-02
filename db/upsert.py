from qdrant_client import QdrantClient
from qdrant_client.http import models
from langchain_qdrant import QdrantVectorStore


# connecting to the client
client = QdrantClient(url="http://localhost:6333")


def upsert_embeddings(collection_name: str, embeddings):

    if not client.collection_exists(collection_name=collection_name):
        # Creating a test collection, which loosely related to being a table in SQL

        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=768, distance=models.Distance.COSINE
            ),
        )
        # Data Insertion, The actual Data would be the vector points, but the payload is just getting associated with it.
        try:
            vector_store = QdrantVectorStore(
                client=client, collection_name=collection_name, embedding=embeddings
            )
        except Exception as e:
            print(e)


def query_collection(collection_name):
    client.query


def delete_collection(collection_name):
    if client.collection_exists(collection_name):
        client.delete_collection(collection_name)
    else:
        return "Collection Doesn't Exist"
