import requests
import wikipediaapi

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"


def get_wiki_stats(search_question):
    params = {
        "action": "opensearch",
        "namespace": "0",
        "search": search_question,
        "limit": "3",
        "format": "json"
    }

    data = S.get(url=URL, params=params).json()

    titles = data[1]

    wiki_wiki = wikipediaapi.Wikipedia('en')

    return list(map(lambda x: (x.title, x.summary[0:200]), [wiki_wiki.page(x) for x in titles]))
