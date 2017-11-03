
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
# Loads the config file
app.config.from_object('config')

# local import
from app import views
