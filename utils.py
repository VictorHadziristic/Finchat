from datetime import date
from typing import TypedDict, Dict, Any, Optional

class ToolCall(TypedDict):
    name: str
    args: Dict[str, Any]
    id: Optional[str]

def get_todays_date():
    """
    Returns today's date in YYYY-MM-DD format.
    """
    return date.today().strftime("%Y-%m-%d")