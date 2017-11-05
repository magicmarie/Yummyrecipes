# local imports
from app import app
from app.models.users import User
from app.models.yummyrecipesapp import Yummy
from flask_wtf import form
from .forms import LoginForm, SignupForm, RecipeForm, CategoryForm

# third party imports
from flask import Flask, flash, render_template, url_for, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

user = Yummy()


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/signup",  methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email not in user.app_users:
            #  creating a user id
            dict_length = len(user.app_users)
            if dict_length == 0:
                id = 1
            id = len(user.app_users) + 1

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
                return redirect(url_for('account'))
    return render_template('login.html', form=form)


@app.route('/account', methods=['GET', 'POST'])
def account():

    return render_template('account.html')
