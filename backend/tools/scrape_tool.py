# backend/tools/scrape_tool.py
import requests
from bs4 import BeautifulSoup
from langchain.tools import Tool

def fetch_page(url: str) -> str:
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent":"agent-bot/1.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # remove scripts/styles for clearer text
        for s in soup(["script","style","noscript"]):
            s.extract()
        text = soup.get_text(separator="\n")
        # optional: keep first N characters
        return text[:20000]
    except Exception as e:
        return f"ERROR: {e}"

scrape_tool = Tool(
    name="fetch_page",
    func=fetch_page,
    description="Fetch HTML content text for a given URL. Input: url. Returns: page text (truncated)."
)
