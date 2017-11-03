class User(object):


""" This allows recipe categories and recipe items to be created and manipulated """


def __init__(self, id, name, username, passsword):
    self.id = id
    self.name = name
    self.username = username
    self.password = password
    self.categories = {}


def get_id(self):


"""This Overrides id to be username"""
    return self.username

"""This creates category """


def create_categories(self, id, recipe_category):
    pass


""" This allows the user to view the catogory list"""


def view_category(self, recipe_category)


if recipe_category in self.categories:
            self.recipe_category[new_category_name] = self.recipe_category[category_name]
            del self.recipe_category[category_name]
            return self.recipe_category


def delete_category(self, id, recipe_category):
     """ This deletes a recipe category"""

        del self.recipe_category[category_name]
        return self.recipe_category

 """ This edits a recipe category"""
def edit_category(self, id, recipe_category )



    def create_recipe(self, recipe_category, recipe_item):
        """ This creates recipe items  in a specified recipe category."""
        the_category = self.recipe_category[category_name]
        new_recipe = recipe_item(recipe_name)
        the_category.recipes[recipe_name] = new_recipe
        return the_category.recipes

    
    def edit_recipe(self, recipe_category, recipe_item, new_recipe_item):
        ''' This edits a recipe item '''
        pass

    def delete_recipe(self, recipe_category, recipe_item):
        """ Deletes a recipe item """

        del self.categories[recipe_category].recipes[recipe_item]
        return self.categories[category_name].recipes
