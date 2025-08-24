# backend/tools/search_tool.py
from ddgs import DDGS
from langchain.tools import Tool

def ddg_search(query: str, max_results: int = 5) -> str:
    """Perform a DuckDuckGo web search and return results as formatted text."""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(f"{r.get('title')}\n{r.get('href')}\n{r.get('body')}\n")
    return "\n\n".join(results) if results else "No results found."

search_tool = Tool(
    name="duckduckgo_search",
    func=lambda q: ddg_search(q, max_results=5),
    description="Use for web searches. Input: search query. Returns titles, snippets, and URLs."
)
