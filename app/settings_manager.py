import json
from flask import session


SETTINGS_FILE = "app/data/settings.json"


def load_settings():
    with open(SETTINGS_FILE, encoding="utf8") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf8") as f:
        json.dump(settings, f, indent=4)