import csv
from flask import Flask, render_template, redirect, request, flash, url_for
from authenticate import authenticate, hash_pw
from database import add_account, get_account
from password_generator import test_password

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
    if request.method == 'POST':
        # USERNAME TAKEN
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            if test_password(password) and password == confirm_password:
                password_hash = hash_pw(password)
                add_account(username, password_hash, 1)
                return redirect(url_for('login'))
            if not test_password(password):
                flash("Password not valid! Please create a stronger password", 'alert-danger')
            else:
                flash("Passwords did not match! Please try again.", 'alert-danger')
        except KeyError:
            pass
    return render_template('signup.html')


@app.route("/home", methods=['GET'])
def home():
    username=request.args.get('username')
    access_lvl = request.args.get('access_lvl')
    flash("Welcome, " + username + "! You have logged in!", "alert-success")
    return render_template('home.html', username=username, access_lvl=access_lvl)
