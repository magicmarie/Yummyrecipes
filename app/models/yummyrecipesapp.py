# Local import
from app.models.users import User

# Third party imports
from flask_login import logout_user
from werkzeug.security import generate_password_hash, check_password_hash


class Yummy(object):

    """ This allows users to sign up, sign in and sign out """
    # class constructor, defines & initialises the attributes

    def __init__(self):
        self.app_users = {}

    def signup(self, email, password):
        """new user sign up """

        # checks if email in our users dictionary
        if email not in self.app_users:
            # hashing the password for security purposes
            hashed = generate_password_hash(password)
            # saving instance of user class in app_users dictionary.email is key

            self.app_users[email] = User(email, hashed)
            return True
        return False

    def login(self, email, password):
        """account login """

        if email in self.app_users:
            hashed_pswd = self.app_users[email].password
            if check_password_hash(hashed_pswd, password):
                return self.app_users[email]
            return "Wrong email/password"
        return "The email does not exist, please signup"

    def create_r(self, username, cat_name, rcep_nm, des):
        usr = app_users[username]
        catgr = usr.categries[cat_name]
        rcpe = Recipe(rcep_nm, des)
        catgr.add_recpie(rcpe)
