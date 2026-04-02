from create_embeddings import pdf_processing_pipeline
from db.upsert import delete_collection
from create_embeddings import generate_embeddings


def main():
    pdf_processing_pipeline("lorem.pdf")
    #delete_collection("pdf_embeddings_collection")


if __name__ == "__main__":
    main()
