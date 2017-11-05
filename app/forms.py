# local imports
from app.models.recipeitem import Recipe
from app.models.users import user
from app.model.yummyrecipeapp import Yummy

# third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class SignupForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('New Password', [validators.Required(
    ), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')


class CategoryForm(FlaskForm):
    Category = StringField('Category:', validators=[DataRequired()])


class RecipeForm(FlaskForm):
    name = StringField('Recipe:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])
