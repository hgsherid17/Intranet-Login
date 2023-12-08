"""
Intranet Login System


This script defines a Flask web application for an intranet system. It includes
routes for user login, signup, and accessing different areas based on access levels.
The application uses Flask sessions to store user information.

Author: Hannah Sheridan
"""
from flask import Flask, render_template, redirect, request, flash, url_for, session
from authenticate import authenticate, hash_pw
from database import add_account, get_account, get_all_accounts, update_last_accessed
from password_generator import test_password, create_strong_password
from intranetLogin import MENU_ACCESS, MENU_OPTIONS, menu_access

app = Flask(__name__, static_folder="instance/static")
app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def login():
    """User Login Page"""
    if request.method == 'POST':
        try:
            # Get user input
            username = request.form.get('username')
            password = request.form.get('password')

            # Match info with stored accounts
            credentials = get_account(username)
            if credentials is not None:
                pw_hash = credentials[0]

                # If passwords match, redirect to home
                if pw_hash is not None and authenticate(pw_hash, password, 40):
                    update_last_accessed(username)
                    session['username'] = username
                    session['access_lvl'] = credentials[1]
                    return redirect(url_for('home'))
        except KeyError:
            pass
        # Flash message if login unsuccessful
        flash("Invalid username or password!", 'alert-danger')
    return render_template('login.html',
                           title="Secure Login",
                           heading="Secure Login")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    """User Sign Up Page"""

    # Generate strong password suggestion
    strong_password = create_strong_password()
    duplicate = False
    if request.method == 'POST':
        # USERNAME TAKEN
        try:
            username = request.form.get('username')
            password = request.form.get('password')

            confirm_password = request.form.get('confirm_password')
            all_users = get_all_accounts()

            if all_users is not None:
                # Check for duplicate usernames
                for user in all_users:
                    if user[0] == username:
                        duplicate = True
                        break

            # If username is taken, print error message
            if duplicate == True:
                flash("Someone already has that username! Please choose a different one", 'alert-danger')
            else:
                # If passwords match and are strong, redirect to login
                if test_password(password) and password == confirm_password:
                    password_hash = hash_pw(password)
                    add_account(username, password_hash, 2)
                    return redirect(url_for('login'))
                # If password not strong, print error message
                if not test_password(password):
                    flash("Password not valid! Please create a stronger password", 'alert-danger')
                else:
                    flash("Passwords did not match! Please try again.", 'alert-danger')
        except KeyError:
            pass
    return render_template('signup.html', generated_password=strong_password)


@app.route("/home", methods=['GET'])
def home():
    """Home Page"""
    username = session.get('username')
    access_lvl = session.get('access_lvl')

    # Issue welcome message and print allowed menu options
    flash("Welcome, " + username + "! Your access level is " + access_lvl, "alert-success")

    allowed_options = MENU_ACCESS[int(access_lvl)]

    return render_template('home.html', menu_options=allowed_options, MENU_OPTIONS=MENU_OPTIONS)


@app.route("/area", methods=['GET'])
def area():
    """Menu Area Page"""

    # Print selected menu option
    option = request.args.get('option')
    username = session.get('username')
    access_lvl = session.get('access_lvl')

    if not menu_access(access_lvl, option):
        flash("Access Denied! Choose a different option.", 'alert-danger')
        return redirect(url_for('home'))

    return render_template('area.html', selected_option=option, MENU_OPTIONS=MENU_OPTIONS, username=username, access_lvl=access_lvl)

