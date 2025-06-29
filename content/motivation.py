import requests

def get_motivation(mood_type="calm"):
    try:
        # You can change the source here if you want spiritual/success quotes
        res = requests.get("https://zenquotes.io/api/random")
        if res.status_code == 200:
            quote = res.json()[0]
            return f"🌟 {quote['q']} — {quote['a']}"
    except:
        pass
    return "🌟 You’re doing great. Keep going!"
