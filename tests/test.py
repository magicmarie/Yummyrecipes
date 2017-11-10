import unittest
# import the module you wanna test
from app import app
import config
from app.models.yummyrecipesapp import Yummy
from app.models.users import User

# inherit from unittest.case wc gives us access to alot of capabilities in that class


class Test_user(unittest.TestCase):

    def setUp(self):
        """This activates the flask testing config flag, disabling
        error catching during request handling.
        The test_client provides an interface to the application.
        """
        self.app = app.test_client(self)
        app.config['WTF_CSRF_ENABLED'] = False
        self.myapp = Yummy()
        self.user = User('magic@gmail.com', '1234')

        self.app.testing = True

    def test_index_page_works_well(self):
        client = app.test_client(self)
        response = client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'MARIAM', response.data)

    def test_sign_up_page_works_well(self):
        client = app.test_client(self)
        response = client.get('/signup', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'YUMMY RECIPES', response.data)

    def test_sign_in_page_works_well(self):
        client = app.test_client(self)
        response = client.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'YUMMY RECIPES', response.data)

    def test_yummyrecipeapp_if_instance(self):
        """ usertest if instance of user is added"""
        self.assertIsInstance(self.myapp, Yummy)

    def test_user_can_login(self):
        user = User('magic@gmail.com', '1234')
        self.myapp.users = {'magic@gmail.com': user}
        response = self.app.post('/login',
                                 data=dict(email='magic@gmail.com', password='1234'), follow_redirects=True)
        self.assertIn(b'magic@gmail.com', response.data)


if __name__ == '__main__':
    unittest.main()
