# local imports
from app import app
from app import login_manager
from app.models.users import User
from app.models.yummyrecipesapp import Yummy
from app.models.categories import Category
from app.models.recipeitem import Recipe
from flask_wtf import form
from .forms import LoginForm, SignupForm, RecipeForm, CategoryForm, EditForm


# third party imports
from flask import flash, render_template, url_for, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

user = Yummy()
category_data = {}

recipe_data = {}

"""route function of the Flask class tells the app which URL should call the
associated function/ could use add_url_rule() too"""
# it binds a URL to a function


@app.route("/")
def main():
    return render_template('index.html')

# Get:Sends data in unencrypted form to the server.
# Post:sends form data to a URL.


@app.route("/signup",  methods=["GET", "POST"])
def signup():
    """ collects form data present in signup.form in a dictionary object and
    sends it for rendering to signup.html."""
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        if email not in user.app_users:

            new_account = user.signup(email, password)
            flash('Account has been created')
            if new_account:
                """ takes you to the login page """
                """ builds a URL for a specific function. The function accepts
                the name of a function as first argument corresponding to the
                variable part of URL."""
                return redirect(url_for('login'))
            flash("Account not created")
    """ Using the Jinja2 template engine to render an html file"""
    return render_template('signup.html', form=form)


# route for handling the login page logic


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email in user.app_users:
            loggedin = user.login(email, password)

            if isinstance(loggedin, User):
                login_user(loggedin)
                return redirect(url_for('account'))
    return render_template('login.html', form=form)


@app.route('/account')
@login_required
def account():
    return render_template('account.html', category_data=category_data)


@app.route('/addcategory', methods=['GET', 'POST'])
@login_required
def addcategory():
    """" addcategory form"""
    form = CategoryForm()
    if form.validate_on_submit():
        category_name = form.category.data
        description = form.description.data
        category = Category(category_name, description)
        category_data[category.name] = category
        return redirect(url_for('account'))

    return render_template('addcategory.html', form=form)


@app.route('/deletecategory/<category_name>', methods=['GET', 'POST'])
@login_required
def deletecategory(category_name):
    """ deletes a category from the category list"""
    if category_name in category_data:
        del category_data[category_name]

    return redirect(url_for('account'))


@app.route('/editcategory/<category_name>', methods=['GET', 'POST'])
@login_required
def editcategory(category_name):
    form = EditForm()
    form.category.data = category_data[category_name].name
    form.description.data = category_data[category_name].description
    category = category_data[category_name]
    if form.validate_on_submit():
        category_new_name = form.category.data
        description_new = form.description.data
        category.name = category_new_name
        category.description = description_new
        return redirect(url_for('account'))
    return render_template('edit.html', form=form, category_name=category_name)


@app.route('/addrecipeitem', methods=['GET', 'POST'])
@login_required
def addrecipeitem():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe_name = form.recipe.data
        description = form.description.data
        recipe_data[recipe_name] = description
        return redirect(url_for('recipelist'))

    return render_template('addrecipeitem.html', form=form)


@app.route('/recipelist', methods=['GET'])
@login_required
def recipelist():
    if request.method == 'GET':
        import pdb
        pdb.set_trace()
        return render_template('recipelist.html', recipe_data=recipe_data)


@login_manager.user_loader
def load_user(email):
    return user.app_users.get(email)  # returns a value for the given key
