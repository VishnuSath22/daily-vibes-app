import requests

API_KEY = "YOUR_NEWS_API_KEY"  # Replace with your real key

def get_news(topics):
    headlines = []
    for topic in topics:
        url = (
            f"https://newsapi.org/v2/top-headlines?"
            f"q={topic}&language=en&pageSize=1&apiKey={API_KEY}"
        )
        try:
            res = requests.get(url)
            if res.status_code == 200:
                articles = res.json().get("articles", [])
                if articles:
                    article = articles[0]
                    headlines.append(f"📰 {article['title']} - {article['source']['name']}")
        except:
            continue

    return headlines or ["⚠️ Couldn't fetch news right now."]
