from langchain_openrouter import ChatOpenRouter


def get_result_from_model(db_result, query):
    model = ChatOpenRouter(model="openrouter/free", temperature=0.7)
    try:
        ask_llm = f"Answer this query: {query} by having this as your context: {db_result}. Analyse the context and correct if possible."
        response = model.invoke(ask_llm)
        return response.content
    except Exception as e:
        error = f"An error occured when invoking the LLM: {e}"
        return error
