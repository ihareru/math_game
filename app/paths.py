import os
import sys
import shutil


if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
    APP_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    APP_DIR = BASE_DIR


DATA_DIR = os.path.join(BASE_DIR, "data")
BACKGROUNDS_DIR = os.path.join(BASE_DIR, "backgrounds")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(BACKGROUNDS_DIR, exist_ok=True)


def copy_default_backgrounds():
    source_dir = os.path.join(APP_DIR, "app", "static", "backgrounds")

    if not os.path.exists(source_dir):
        return

    for filename in os.listdir(source_dir):
        src = os.path.join(source_dir, filename)
        dst = os.path.join(BACKGROUNDS_DIR, filename)

        if not os.path.exists(dst):
            shutil.copy2(src, dst)