from datetime import date
from typing import TypedDict, Dict, Any, Optional
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_core.tools import tool
from bs4 import BeautifulSoup

import os

os.environ['USER_AGENT'] = 'myagent'

@tool
def scrape_url(url: str) -> str:
    """
    Scrapes the content of a specified URL using an asynchronous Chromium-based loader.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: The loaded content from the specified URL.

    Example:
        content = scrape_url("https://example.com")
    """
    loader = AsyncChromiumLoader([url])
    docs = loader.load()

    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    return docs_transformed[0].page_content[0:1000]

class ToolCall(TypedDict):
    name: str
    args: Dict[str, Any]
    id: Optional[str]

def get_todays_date():
    """
    Returns today's date in YYYY-MM-DD format.
    """
    return date.today().strftime("%Y-%m-%d")