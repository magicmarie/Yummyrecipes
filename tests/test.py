import unittest
# import the module you wanna test
from app import app
import config
from app.models.yummyrecipesapp import Yummy
from app.models.users import User

# inherit from unittest.case wc gives us access to alot of capabilities in that clas


class Test_user(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client(self)
        app.config['WTF_CSRF_ENABLED'] = False

        self.app.testing = True

    def test_index_page_works_well(self):
        client = app.test_client(self)
        response = client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'MARIAM', response.data)

    def sign_up_page_works_well(self):
        client = app.test_client(self)
        response = client.get('/signup', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'YUMMY RECIPES', response.data)

    def sign_in_page_works_well(self):
        client = app.test_client(self)
        response = client.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'YUMMY RECIPES', response.data)

    def unauthenticated_user_cant_view_account(self):
        client = app.test_client(self)
        response = client.get('/account', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        # user = Yummy('m@gmail.com', 'magic')
        # """response = client.post('/signup', data=dict(
        #     name='mariam'
        #     email='m@gmail.com'
        #     password='magic'
        #     confirm='magic'
        # ))"""


if __name__ == '__main__':
    unittest.main()
