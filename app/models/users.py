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

    def create_categories(self, id, recipe_category):
        """This creates category """
        if recipe_category not in self.categories:
            new_category = Category(recipe_category)
            self.categories[recipe_category] = new_category
            return self.categories
        return "category not created"

    def view_category(self, recipe_category):
        """ This allows the user to view the catogory list"""

        if recipe_category in self.categories:
            self.recipe_category[new_category_name] = self.recipe_category[category_name]
            del self.recipe_category[category_name]
            return self.recipe_category

    def delete_category(self, id, recipe_category):
        """ This deletes a recipe category"""

        del self.recipe_category[category_name]
        return self.recipe_category

    def edit_category(self, id, recipe_category):
        """ This edits a recipe category"""

    def create_recipe(self, recipe_category, recipe_item):
        """ This creates recipe items  in a specified recipe category."""
        pass

    def edit_recipe(self, recipe_category, recipe_item, new_recipe_item):
        ''' This edits a recipe item '''
        pass

    def delete_recipe(self, recipe_category, recipe_item):
        """ Deletes a recipe item """
        pass
