

import requests

NEWS_API_KEY = "e6877a99408840588a135a6f16fb2573"  # 🔒 Replace with your real key

def get_latest_industry_trends(industry: str, max_results: int = 5) -> list:
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": industry,
        "language": "en",
        "pageSize": max_results,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        articles = response.json().get("articles", [])
        headlines = [article["title"] for article in articles if article.get("title")]

        if not headlines:
            return ["No relevant headlines found."]
        
        return headlines

    except requests.exceptions.RequestException as e:
        return [f"Network error: {str(e)}"]

    except Exception as e:
        return [f"Unexpected error: {str(e)}"]
