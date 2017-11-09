from app.models.recipeitem import Recipe

class Category(object):

    """ This holds the recipe category details"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.category_data = {}

    def get_name(self):
        return self.name

    def set_category(self, name, description):
        self.name = name
        self.description = description

    def create_recipe(self, rcepe):
        """ This creates recipe items  in a specified recipe category."""
        self.recipes[rcepe.name] = rcepe
        pass

    def edit_recipe(self, recipe_category, recipe_item, new_recipe_item):
        ''' This edits a recipe item '''
        if recipe_item in self.recipes:
            self.recipes[new_recipe_item] = self.recipes.pop(recipe_item)
            return True
        return False

    def delete_recipe(self, recipe_category, recipe_item):
        """ Deletes a recipe item """
        if recipe_item in self.recipes:
            self.recipes.pop(recipe_item)
            return True
        return False
