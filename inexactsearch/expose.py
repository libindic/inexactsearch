from inexactsearch import InexactSearch


def inexactsearch_search(text, key):
    return InexactSearch().search(text, key)


def search():
    return [inexactsearch_search, str, str, [str]]
