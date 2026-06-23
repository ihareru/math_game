import json
import os

SETTINGS_FILE = "app/data/settings.json"

# DEFAULT_SETTINGS = {
#     "background_color": "#87CEEB",
#     "background_image": "",
#     "theme": "light",

#     "background_music": True,
#     "success_sound": True,
#     "fail_sound": True
# }


def load_settings():
    try:
        with open(SETTINGS_FILE, encoding="utf8") as f:
            return json.load(f)

    except:
        settings = {
            "background_color": "#87CEEB",
            "background_image": "",
            "theme": "light",

            "background_music": True,
            "success_sound": True,
            "fail_sound": True
        }

        save_settings(settings)

        return settings


def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf8") as f:
        json.dump(settings, f, indent=4)