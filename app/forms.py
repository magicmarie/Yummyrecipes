# local imports
from app.models.recipeitem import Recipe
from app.models.users import User
from app.models.yummyrecipesapp import Yummy

# third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Users log into their accounts """
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class SignupForm(FlaskForm):
    """ This allows users to create accounts"""
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('New Password', [validators.Required(
    ), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    """print("....", name, email, password, confirm)"""


class EditForm(FlaskForm):
    """ Editing the category"""
    category = StringField('Category:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])


class CategoryForm(FlaskForm):
    """creates a recipe category  """
    category = StringField('Category:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])


class RecipeForm(FlaskForm):
    """ creates a recipe item"""
    recipe = StringField('Recipe:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])
