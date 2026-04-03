from create_embeddings import pdf_processing_pipeline
from db.upsert import delete_collection
from db.upsert import query_collection
from query_llm import get_result_from_model

COLLECTION_NAME = "pdf_embeddings_collection"


def main():
    # pdf_processing_pipeline("QA.pdf")
    query = str(input("What do you want to ask about this pdf?: \n"))
    query_result = query_collection(
        collection_name=COLLECTION_NAME,
        query_text=query,
        limit=5,
    )
    context_texts = [
        point.payload["text_str"] for point in query_result if point.payload
    ]
    if not context_texts:
        print("No relevant context found.")
        return
    context = "\n\n---\n\n".join(context_texts)
    llm_result = get_result_from_model(db_result=context, query=query)
    print(llm_result)


if __name__ == "__main__":
    main()
