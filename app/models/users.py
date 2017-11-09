# local imports
from app.models.categories import Category


# third party imports
from flask_login import UserMixin


class User(UserMixin):
    """ This allows recipe categories and recipe items to be created and
    manipulated """

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.categories = {}

    def get_id(self):
        return self.email

    def delete_category(self, recipe_category):
        """ This deletes a recipe category"""
        if recipe_category in self.categories:
            self.categories.pop(recipe_category)
            return True
        return False

    def edit_category(self, recipe_category, new_recipe_category):
        """ This edits a recipe category"""
        if recipe_category in self.categories:
            self.categories[new_recipe_category] = self.categories.pop(
                recipe_category)
            return True
        return False
