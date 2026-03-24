import requests
import json
import os
from datetime import datetime

BEARER_TOKEN = os.environ.get("X_BEARER_TOKEN")

def search_recent_posts(query: str, max_results: int = 20) -> dict:
    """Search recent X posts using the v2 API."""
    url = "https://api.x.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {
        "query": query,
        "max_results": min(max_results, 100),
        "tweet.fields": "created_at,public_metrics,author_id,text",
        "expansions": "author_id",
        "user.fields": "name,username",
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "bitcoin institutional"
    print(f"Searching for: {query}")
    results = search_recent_posts(query)
    with open("posts.json", "w") as f:
        json.dump(results, f, indent=2)
    tweets = results.get("data", [])
    print(f"Found {len(tweets)} posts.")
    for tweet in tweets:
        print(f"  [{tweet["created_at"][:10]}] {tweet["text"][:100]}...")