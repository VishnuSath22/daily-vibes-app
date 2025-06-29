import json

def load_users():
    try:
        with open("user_data.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_user(user_id, prefs, update=False):
    users = load_users()
    if update and user_id in users:
        users[user_id].update(prefs)
    else:
        users[user_id] = prefs
    with open("user_data.json", "w") as f:
        json.dump(users, f, indent=2)
