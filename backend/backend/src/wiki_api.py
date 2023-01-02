import os
from requests import Session
import wikipediaapi


def get_wiki_search_results(query: str, session: Session) -> list[dict[str, str]]:
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "namespace": "0",
        "search": query,
        "limit": "3",
        "format": "json",
    }
    headers = {
        "Authorization": f"Bearer {os.getenv('WIKI_BEARER_TOKEN')}",
        "User-Agent": f"mini-oracle ({os.getenv('WIKI_EMAIL')})",
    }

    if not query:
        raise ValueError("Empty query")

    data = session.get(url=url, params=params, headers=headers).json()

    if isinstance(data, dict) and "error" in data:
        raise RuntimeError(data["error"])

    titles = data[1]
    wiki = wikipediaapi.Wikipedia("en", headers=headers)
    pages = [wiki.page(x) for x in titles]
    return [{"title": x.title, "summary": x.summary[0:300]} for x in pages]
