from flask import Flask

app = Flask(__name__)
app.secret_key = 'your-super-secret-key'

from app import routes  # импорт маршрутов (если есть)
