# local imports
from app import app
from app import login_manager
from app.models.users import User
from app.models.yummyrecipesapp import Yummy
from flask_wtf import form
from .forms import LoginForm, SignupForm, RecipeForm, CategoryForm


# third party imports
from flask import Flask, flash, render_template, url_for, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

user = Yummy()

# route function of the Flask class tells the app which URL should call the associated function.
# it binds a URL to a function

#


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/signup",  methods=["GET", "POST"])
def signup():
    form = SignupForm()
    print("???", form)
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        print(">>", email, password, name)
        if email not in user.app_users:

            new_account = user.signup(email, password)
            flash('Account has been created')
            if new_account:
                """ takes you to the login page """
                return redirect(url_for('login'))
            flash("Account not created")

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


@app.route('/account', methods=['GET', 'POST'])
def account():

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email in user.app_users:
            loggedin = user.login(email, password)

            if isinstance(loggedin, User):
                return redirect(url_for('account'))
        return render_template('login.html', form=form)
    return render_template('account.html')


'''
@app.route("/settings")
@login_required
def settings():
    pass


@app.route("/logout")
@login_required
def logout():
    """When the user is ready to log out"""
    logout_user()
    return redirect(somewhere) '''


@login_manager.user_loader
def load_user(email):
    return user.app_users.get(email)  # returns a value for the given key
