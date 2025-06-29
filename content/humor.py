import requests

def get_humor(humor_type="memes"):
    try:
        res = requests.get("https://meme-api.com/gimme")
        if res.status_code == 200:
            meme = res.json()
            return f"{meme['title']}\n{meme['url']}"
    except:
        pass
    return "😅 Here’s a joke: I told my computer I needed a break, and it said 'No problem. I’ll crash.'"
