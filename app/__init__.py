from flask import Flask
from app.settings_manager import load_settings
from app.utils import resource_path
from app.paths import copy_default_backgrounds

app = Flask(__name__, template_folder=resource_path("app/templates"),
            static_folder=resource_path("app/static"))
copy_default_backgrounds()
app.secret_key = 'your-super-secret-key'


@app.context_processor
def inject_settings():
    return dict(
        settings=load_settings()
    )


from app import routes
