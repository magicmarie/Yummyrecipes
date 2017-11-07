class Category(object):

    """ This holds the recipe category details"""

    def __init__(self, recipe_category):
        self.recipe_category = recipe_category
        self.recipes = {}
