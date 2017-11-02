from app import app
from flask import Flask, render_template, url_for


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/login")
def login():
    return render_template('login.html')
