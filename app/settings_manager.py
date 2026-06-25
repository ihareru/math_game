import json
import os
from app.paths import DATA_DIR

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")

SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")

def load_settings():

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(SETTINGS_FILE):

        default = {
            "background_color": "#87CEEB",
            "background_image": "",
            "background_music": True,
            "success_sound": True,
            "fail_sound": True,
            "background_volume": 50,
            "success_volume": 50,
            "fail_volume": 50
        }

        save_settings(default)

        return default

    with open(SETTINGS_FILE, encoding="utf8") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf8") as f:
        json.dump(settings, f, indent=4)



