from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 3):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(f"{r['title']}: {r['body']}")

    return "\n\n".join(results)