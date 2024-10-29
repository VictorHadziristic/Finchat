from datetime import date
from typing import TypedDict, Dict, Any, Optional
from langchain_core.tools import tool
from requests_html import HTMLSession
from bs4 import BeautifulSoup

import os

@tool
def scrape_url(url: str) -> str:
    """
    Scrapes the content of a specified URL using requests_html with custom headers,
    enabling JavaScript to render content.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: The loaded content from the specified URL.

    Example:
        content = scrape_url("https://example.com")
    """
    headers = {
        "User-Agent": "Victor Hadziristic victor.hadziristic@gmail.com",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.sec.gov"
    }
    
    session = HTMLSession()
    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.html.html, "html.parser")
    text_content = soup.get_text()

    return text_content[:10000]


class ToolCall(TypedDict):
    name: str
    args: Dict[str, Any]
    id: Optional[str]

def get_todays_date():
    """
    Returns today's date in YYYY-MM-DD format.
    """
    return date.today().strftime("%Y-%m-%d")