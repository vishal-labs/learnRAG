### The project Flow expectation

1. Store a pdf.
2. Create a langchain helper function, which processes the pdf into embeddings
3. The embeddings are stored in the database
4. Finally, The LLM can use the DB to answer questions that we ask it.

### Questions that I have

1. How to process the PDFs?(currently imagine, the PDFs contain only text)
2. Once the embeddings are created, how to create the required collection for upserting the data?
3. Finally, how will the LLMs use this DB to answer our questions? via MCP? or something else?

### Execution Plan

1. create the processing pipeline
2. once the pdf is converted to embeddings, add it to the DB
3. Learn how to the LLM can access the DB(and probably set it's context only to the PDF)
