# Local import
from app.models.users import User

# Third party imports
from flask_login import logout_user
from werkzeug.security import generate_password_hash, check_password_hash


class Yummy(object):

    """ This allows users to sign up, sign in and sign out """

    def __init__(self):
        self.app_users = {}

    def signup(self, email, password):
        """new user sign up """
        if email not in self.app_users:
            hashed = generate_password_hash(password)
            self.app_users[email] = User(id, email, hashed)
            return True
        return False

    def login(self, email, password):
        """account login """

        if email in self.app_users:
            hashed = self.app_users[email].hashed
            if check_password_hash(hashed, password):
                return self.app_users[email]
            return "Wrong email/password"
        return "The email does not exist, please signup"
