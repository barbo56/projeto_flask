from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
#csrf = CSRFProtect(app) Proteção de alguma coisa que eu não entendi muito bem

from app import routes