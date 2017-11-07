# local imports
from app.models.categories import Category
from app.models.recipeitem import Recipe

# third party imports
from flask_login import UserMixin


class User(UserMixin):
    """ This allows recipe categories and recipe items to be created and
    manipulated """

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
        self.categories = {}

    def get_id(self):
        return self.email

    def create_categories(self, id, recipe_category):
        """This creates category """
        pass

    def view_category(self, recipe_category):
        """ This allows the user to view the catogory list"""
        pass

    def delete_category(self, id, recipe_category):
        """ This deletes a recipe category"""
        pass

    def edit_category(self, id, recipe_category):
        """ This edits a recipe category"""
        pass

    def create_recipe(self, recipe_category, recipe_item):
        """ This creates recipe items  in a specified recipe category."""
        pass

    def edit_recipe(self, recipe_category, recipe_item, new_recipe_item):
        ''' This edits a recipe item '''
        pass

    def delete_recipe(self, recipe_category, recipe_item):
        """ Deletes a recipe item """
        pass
