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
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('New Password', [validators.Required(
    ), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')


class CategoryForm(FlaskForm):
    """creates a category """
    Category = StringField('Category:', validators=[DataRequired()])


class RecipeForm(FlaskForm):
    """ creates a recipe item"""
    name = StringField('Recipe:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])
