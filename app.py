import csv
from flask import Flask, render_template, redirect, request, flash, url_for, session
from authenticate import authenticate, hash_pw
from database import add_account, get_account, get_all_accounts
from password_generator import test_password, create_strong_password

app = Flask(__name__, static_folder="instance/static")
app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def login():
    # with open(app.config['CREDENTIALS_FILE']) as fh:
    #     reader = csv.DictReader(fh)
    #     credentials = {row['username']:
    #                        {'password_hash': row['password_hash'],
    #                        'access_lvl': row['access_lvl']}
    #                   for row in reader}
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            credentials = get_account(username)
            if credentials is not None:
                pw_hash = credentials[0]
            # pw_hash = credentials[username]['password_hash']
                if pw_hash is not None and authenticate(pw_hash, password, 40):
                    return redirect(url_for('home', username=username, access_lvl=credentials[1]))
        except KeyError:
            pass
        flash("Invalid username or password!", 'alert-danger')
    return render_template('login.html',
                           title="Secure Login",
                           heading="Secure Login")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    generated_password = ""
    duplicate = False
    if request.method == 'POST':
        # USERNAME TAKEN
        try:
            # Generate strong password suggestion
            generated_password = request.form.get('generated_password')

            username = request.form.get('username')
            password = request.form.get('password')

            confirm_password = request.form.get('confirm_password')
            all_users = get_all_accounts()

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
                    add_account(username, password_hash, 1)
                    return redirect(url_for('login'))
                # If password not strong, print error message
                if not test_password(password):
                    flash("Password not valid! Please create a stronger password", 'alert-danger')
                else:
                    flash("Passwords did not match! Please try again.", 'alert-danger')
        except KeyError:
            pass
    return render_template('signup.html', generated_password=generated_password)


@app.route("/home", methods=['GET'])
def home():
    username=request.args.get('username')
    access_lvl = request.args.get('access_lvl')
    flash("Welcome, " + username + "! You have logged in!", "alert-success")
    return render_template('home.html', username=username, access_lvl=access_lvl)


@app.route("/generate_password", methods=['GET'])
def generate_password():
    strong_password = create_strong_password()
    session['generated_password'] = strong_password
    return redirect(url_for('signup'))
