"""
Here, we first use process_pipeline function to ingest the pdfs and transform them to the required format
next, we use the embeddings object to get the PDF's embeddings
"""

from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from embeddings import embeddings
from db.upsert import upsert_embeddings

COLLECTION_NAME = "pdf_embeddings_collection"
BATCH_SIZE = 20


def pdf_processing_pipeline(pdf_name: str, batch_size: int = BATCH_SIZE):
    pdf_base_path = "./example-data/pdfs/"
    current_pdf = f"{pdf_base_path}/{pdf_name}"
    loader = PyPDFLoader(current_pdf)
    document = loader.load()
    total_pages = len(document)

    text_splitter = SemanticChunker(
        embeddings=embeddings, breakpoint_threshold_type="percentile"
    )

    total_chunks = 0
    num_batches = (total_pages + batch_size - 1) // batch_size

    for i in range(0, total_pages, batch_size):
        batch_end = min(i + batch_size, total_pages)
        batch_num = (i // batch_size) + 1

        batch_pages = document[i:batch_end]
        split_pages = text_splitter.split_documents(batch_pages)

        texts_list = [doc.page_content for doc in split_pages]

        if texts_list:
            embeddings_list = embeddings.embed_documents(texts_list)
            upsert_embeddings(COLLECTION_NAME, embeddings_list, texts_list)
            total_chunks += len(embeddings_list)
            print(
                f"Batch {batch_num}/{num_batches}: "
                f"Pages {i + 1}-{batch_end} | "
                f"{len(embeddings_list)} chunks | "
                f"Total so far: {total_chunks}"
            )

    print(f"\nDone. Inserted {total_chunks} total chunks into DB")
