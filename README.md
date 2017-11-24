
# YUMMYRECIPES
This is a simple web application set to help you store your recipes. It allows users to sign up for a new  account and login to create and save recipes.

## Features

This application has the following features:

* A user can signup for an account
* A user can  log in with their credentials
* A user can create, edit, and delete categories and or recipes

## Setup

To use the application, ensure that you have python 3.6+,pip3,virtualenv installed on your machine.

You can install grab this repository in two ways

__1.Open your git commandline and clone the repository to your local machine__. 

```sh
    git clone https://github.com/magicmarie/Yummyrecipes.git
```

__2.Or simply browse to [Github](https://github.com/magicmarie/Yummyrecipes.git) and download the project manually__


Enter the project directory

    cd Yummyrecipes

Create a virtual environment

    virtualenv venv

Activate the virtual environment

    source venv/bin/activate

Then install all the required dependencies

    pip install -r requirements.txt

* To start the application run:
    * On windows, Open your terminal
        * set FLASK_CONFIG=development
        * set FLASK_APP=run.py
        * flask run
        * browse to localhost:5000
    * on unix like  os , Open your terminal
        * export FLASK_CONFIG=development
        * export FLASK_APP=run.py
        * flask run
        * browse to localhost:5000
