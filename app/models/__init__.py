# app/models/__init__.py

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()      # creates instance of loginManager
login_manager.init_app(app)         # initialises login manager
login_manager.login_view = 'login'  # links to the login view


from app import views
