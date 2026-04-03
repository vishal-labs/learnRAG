from create_embeddings import pdf_processing_pipeline
from db.upsert import delete_collection
from db.upsert import query_collection
from query_llm import get_result_from_model


def main():
    pdf_processing_pipeline("QA.pdf")
    query = str(input("What do you want to ask about this pdf?: \n"))
    query_result = query_collection(
        collection_name="pdf_embeddings_collection",
        query_text=query,
        limit=2,
    )
    payloads = []
    for point in query_result:
        payloads.append(point.payload)
    llm_result = get_result_from_model(db_result=payloads, query=query)
    print(llm_result)


if __name__ == "__main__":
    main()
