from flask import Flask
from app.settings_manager import load_settings


app = Flask(__name__)
app.secret_key = 'your-super-secret-key'


@app.context_processor
def inject_settings():

    return dict(
        settings=load_settings()
    )

from app import routes  # импорт маршрутов (если есть)
