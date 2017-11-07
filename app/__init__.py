
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
# Loads the config file
app.config.from_object('config')

login_manager = LoginManager()     # creates instance of LoginManager
login_manager.init_app(app)         # initialises login manager
login_manager.login_view = 'login'  # links to the login view


# local import
from app import views
