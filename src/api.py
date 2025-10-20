from __future__ import annotations
from typing import List, Optional
import requests

BASE_URL = "https://api.chucknorris.io"

class ApiError(Exception):
    """Raised when the Chuck Norris API request fails or returns invalid data."""

def _get(path: str, params: Optional[dict] = None) -> dict | list:
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        raise ApiError(f"Network error: {e}") from e
    except ValueError as e:
        raise ApiError("Invalid JSON response from API.") from e

def get_random_joke(category: Optional[str] = None) -> str:
    params = {"category": category} if category else None
    data = _get("/jokes/random", params)
    return str(data.get("value", "")).strip()

def get_categories() -> List[str]:
    data = _get("/jokes/categories")
    if not isinstance(data, list):
        raise ApiError("Unexpected response for categories.")
    return [str(c) for c in data]

def search_jokes(query: str) -> List[str]:
    if not query or not query.strip():
        raise ValueError("query cannot be empty")
    data = _get("/jokes/search", {"query": query})
    results = data.get("result", [])
    return [str(item.get("value", "")).strip() for item in results]
