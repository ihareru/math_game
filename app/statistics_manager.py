import json

FILE = "app/data/statistics.json"


def load_statistics():
    with open(FILE, encoding="utf8") as f:
        return json.load(f)


def save_statistics(stat):
    with open(FILE, "w", encoding="utf8") as f:
        json.dump(stat, f, indent=4)