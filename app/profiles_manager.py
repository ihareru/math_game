import json

from app.paths import DATA_DIR

import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")

PROFILE_FILE = os.path.join(DATA_DIR, "profiles.json")

def load_profiles():

    # создаём папку data
    os.makedirs(os.path.dirname(PROFILE_FILE), exist_ok=True)

    # если файла нет — создаём пустой
    if not os.path.exists(PROFILE_FILE):
        save_profiles([])

    with open(PROFILE_FILE, encoding="utf8") as f:
        return json.load(f)

def save_profiles(profiles):
    with open(PROFILE_FILE, "w", encoding="utf8") as f:
        json.dump(profiles, f, indent=4, ensure_ascii=False)