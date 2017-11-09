
import unittest

from app import app
import config
from app.models.yummyrecipesapp import Yummy
from app.models.users import User


class YummpyrecipeAppTestCase(unittest.TestCase):

    def setUp(self):
        self.myapp = Yummy()
        self.user = User('magic', '1234')

    def test_yummyrecipeapp_if_instance(self):
        self.assertIsInstance(self.myapp, Yummy)
