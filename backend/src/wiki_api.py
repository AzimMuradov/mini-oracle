import wikipediaapi


def get_wiki_search_results(query, session):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "namespace": "0",
        "search": query,
        "limit": "3",
        "format": "json"
    }

    if not query:
        raise ValueError('empty query')

    data = session.get(url=url, params=params).json()

    if isinstance(data, dict) and 'error' in data:
        raise ValueError(data['error'])

    titles = data[1]
    wiki = wikipediaapi.Wikipedia('en')
    pages = [wiki.page(x) for x in titles]
    return [{'title': x.title, 'summary': x.summary[0:200]} for x in pages]
