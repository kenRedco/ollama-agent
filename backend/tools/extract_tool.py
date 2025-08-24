# backend/tools/extract_tool.py
import re
from langchain.tools import Tool

def extract_emails(text: str) -> str:
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    unique = list(dict.fromkeys(emails))
    return "\n".join(unique) if unique else "NO_EMAILS_FOUND"

extract_emails_tool = Tool(
    name="extract_emails",
    func=extract_emails,
    description="Extract email addresses from a block of text."
)
