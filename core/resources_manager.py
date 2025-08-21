import requests

def fetch_cyber_news():
    try:
        url = "https://newsapi.org/v2/everything?q=cybersecurity&apiKey=demo"  # Replace demo with real key
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])[:5]
            return [{"title": a["title"], "source": a["source"]["name"], "url": a["url"], "date": a["publishedAt"]} for a in articles]
    except:
        return []
    return []
