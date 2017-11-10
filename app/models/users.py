# local imports
from app.models.categories import Category
from app.models.recipeitem import Recipe


# third party imports
from flask_login import UserMixin


class User(UserMixin):
    """ This allows recipe categories and recipe items to be created and
    manipulated, the UserMixin package will give the User class
    some pre-built functionality to do with user login tasks, mixing in
    some attributes to your person  """

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.category_data = {}

    def get_id(self):
        return self.email

    def create_category(self, category_name, description):
        """Creates the Category,Takes in two parameters,creates an instance of
        the class category and adds it to the categories dictionary"""

        if not isinstance(category_name, description):
            if category_name not in self.category_data:
                new_category = Category(category_name, description)
                self.category_data[category_name] = new_category
                return self.category_data
            return "that category already exists"

    def edit_category(self, category_name, description):
        updated_category = Category(category_name, description)
        self.category_data[category_name] = updated_category

    def delete_category(self, category_name):
        del self.category_data[category_name]
        return self.category_data

    def create_recipe(self, category_name, recipe_name, description):
        the_category = self.category_data[category_name]
        new_recipe = Recipe(recipe_name, description)
        the_category.recipes[recipe_name] = new_recipe
        return the_category.recipes

    def view_recipes(self, category_name):
        all_recipes = self.category_data[category_name].recipes
        return all_recipes

    def edit_recipe(self, category_name, recipe_name, ingredients):
        the_recipes = self.category_data[category_name].recipes
        updated_recipe = Recipe(category_name, ingredients)
        the_recipes[recipe_name] = updated_recipe

    def delete_recipe(self, category_name, recipe_name):
        """Deletes a recipe,takes in two attributes, checks categories
        dictionary for key category_name. checks the recipes list in the
        category for the recipe name. deletes the recipe and returns
        The list in the category instance"""

        del self.category_data[category_name].recipes[recipe_name]
        return self.category_data[category_name].recipes
