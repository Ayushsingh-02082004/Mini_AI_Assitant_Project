from agent.agent import llm
from agent.tools import document_search


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    context = document_search.invoke(question)

    prompt = f"""
    Answer the question using the context.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm(prompt)

    print("\nAssistant:")
    print(response[0]["generated_text"])