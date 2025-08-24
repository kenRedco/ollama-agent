import re
import requests
from bs4 import BeautifulSoup
from langchain.tools import Tool

def scrape_emails_from_url(url: str, timeout: int = 10) -> str:
    """Scrape emails from a given webpage URL."""
    try:
        response = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            return f"Failed to fetch {url} (status {response.status_code})"
        
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()

        # regex for emails
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text))
        if not emails:
            return f"No emails found on {url}"
        return f"Emails from {url}: {', '.join(emails)}"
    
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

email_scraper_tool = Tool(
    name="email_scraper",
    func=scrape_emails_from_url,
    description="Extracts email addresses from a given website URL. Input: a single URL."
)
