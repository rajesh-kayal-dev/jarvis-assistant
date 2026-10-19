
from jarvis.config import NEWS_API_KEY

import requests





class NewsService:
    def get_headlines(self) -> list[str]:
        api_key = NEWS_API_KEY

        if not api_key:
            raise ValueError("NEWS_API_KEY is missing. Check your .env file.")

        response = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={
                "country": "in",
                "apiKey": api_key,
            },
            timeout=10,
        )
        response.raise_for_status()

        data = response.json()
        articles = data.get("articles", [])

        return [
            article["title"]
            for article in articles
            if article.get("title")
        ]
