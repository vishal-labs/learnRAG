"""
Here, we first use process_pipeline function to ingest the pdfs and transform them to the required format
next, we use the generate_embeddings function to get the PDF's embeddings
"""

import os
import numpy as np
import requests
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.pdf import PyPDFLoader

from db.upsert import upsert_embeddings

load_dotenv()

collection_name = "pdf_embeddings_collection"


def pdf_processing_pipeline(pdf_name: str):
    pdf_base_path = "./example-data/pdfs/"
    current_pdf = f"{pdf_base_path}/{pdf_name}"
    loader = PyPDFLoader(current_pdf)
    document = loader.load()
    # Chunking the data and creating embeddings
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=100)
    split_pages = text_splitter.split_documents(document)
    for i, doc in enumerate(split_pages):
        embeddings = generate_embeddings(doc.page_content)
        upsert_embeddings(collection_name, embeddings)
        print(f"{i}th embedding inserted into DB")


def generate_embeddings(payload: str):
    OLLAMA_IP = os.getenv("OLLAMA_PROVIDER_IP")
    request_url = f"http://{OLLAMA_IP}:11434/api/embed"
    try:
        response = requests.post(
            request_url,
            json={"model": "nomic-embed-text", "input": payload},
            timeout=30,
        )
        embeddings = np.array(response.json()["embeddings"], dtype=np.float32)
        return embeddings.shape
    except Exception as e:
        print(e)
