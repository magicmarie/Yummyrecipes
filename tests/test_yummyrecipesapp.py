# third party imports
import unittest

# local imports
from app.models.yummyrecipesapp import Yummy
from app.models.users import User


class YummpyrecipeAppTestCase(unittest.TestCase):

    def setUp(self):
        self.myapp = Yummy()
        self.user = User('magic', '1234')

    def test_yummyrecipeapp_if_instance(self):
        self.assertIsInstance(self.myapp, Yummy)

    """def test_yummy_if_user_can_sign_up(self):
        ''' Test if a user can sign up '''
        self.myapp.signup(self.user)
        self.assertIn(self.user.username, self.myapp.users)
"""
