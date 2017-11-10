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
