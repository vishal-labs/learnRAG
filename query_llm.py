from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate


def get_result_from_model(db_result, query):
    model = ChatOpenRouter(model="openrouter/free", temperature=0.7)
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant that answers questions based on the provided context. Keep the answers consise and simple. Let the user know if the answer from context or not",
                ),
                ("user", "Context: {context}\n\nQuestion: {question}\n\nAnswer:"),
            ]
        )
        # Invoke with variables
        formatted = prompt.invoke({"context": db_result, "question": query})
        response = model.invoke(formatted)
        return response.content
    except Exception as e:
        error = f"An error occured when invoking the LLM: {e}"
        return error
