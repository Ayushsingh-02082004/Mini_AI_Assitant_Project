from langchain.tools import tool
from rag.retriever import retriever

@tool
def document_search(query: str) -> str:
    """
    Search uploaded documents.
    """

    docs = retriever.invoke(query)

    return "\n".join(
        doc.page_content
        for doc in docs[:3]
    )