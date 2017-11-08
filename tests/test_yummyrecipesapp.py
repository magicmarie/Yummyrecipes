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

    def test_yummy_if_user_can_sign_up(self):
        ''' Test if a user can sign up '''
        self.myapp.signup(self.user)
        self.assertIn(self.user.username, self.myapp.users)

        """ def test_yummyrecipeapp_if_user_email_exists(self):
           ''' Test if email is already taken '''

           self.new_user = User('username', 'password')
           self.myapp.signup(self.the_user)
           potential_user = self.myapp.signup(self.new_user)
           self.assertFalse(potential_user, msg='That username already exists')

    def test_yummyapp_if_user_can_sign_in(self):
           ''' Test if existing user can sign in if their credentials match '''

           self.myapp.signup(self.the_user)
           self.myapp.signin('username', 'password')
           ''' print(signed_in) '''
           self.assertEqual('password', self.the_users['username'].hashed_pswd,
                            msg='The username and password combination does not \
                           exist')

       def test_yummyapp_if_user_can_logout(self):
           pass  """
