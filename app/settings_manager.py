import json
import os

SETTINGS_FILE = "app/data/settings.json"

DEFAULT_SETTINGS = {
    "background_type": "color",
    "background_color": "#87CEEB",
    "background_image": "",
    "theme": "light",
    "sound": True
}


def load_settings():

    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

    try:
        with open(SETTINGS_FILE, encoding="utf8") as f:
            return json.load(f)

    except Exception:
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS


def save_settings(settings):

    with open(SETTINGS_FILE, "w", encoding="utf8") as f:
        json.dump(settings, f, indent=4)