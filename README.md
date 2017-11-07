
# YUMMYRECIPES
This is a simple web application set to help you store your recipes. It allows users to sign up for a new  account and login to create and save recipes.

## Features

This application has the following features:

* A user can signup for an account
* A user can  log in with their credentials
* A user can create, edit, and delete categories and or recipes

## Setup

To use the application, ensure that you have python 3.6+, clone the repository to your local machine. Open your git commandline and run

    git clone https://github.com/magicmarie/Yummyrecipes.git

Enter the project directory

    cd Yummyrecipes

Create a virtual environment

    virtualenv venv

Activate the virtual environment

    source venv/bin/activate

Then install all the required dependencies

    pip install -r requirements.txt

To start the application run:

    set FLASK_CONFIG=development
    set FLASK_APP=run.py
    flask run
