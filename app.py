import csv
from flask import Flask, render_template, redirect, request, flash, url_for
from authenticate import authenticate, hash_pw
from database import add_account

app = Flask(__name__, static_folder="instance/static")
app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def login():
    with open(app.config['CREDENTIALS_FILE']) as fh:
        reader = csv.DictReader(fh)
        credentials = {row['username']:
                           {'password_hash': row['password_hash'],
                            'access_lvl': row['access_lvl']}
                       for row in reader}
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            pw_hash = credentials[username]['password_hash']
            if authenticate(pw_hash, password, 40):
                return redirect(url_for('home', username=username, access_lvl=credentials[username]['access_lvl']))
        except KeyError:
            pass
        flash("Invalid username or password!", 'alert-danger')
    return render_template('login.html',
                           title="Secure Login",
                           heading="Secure Login")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        ## USERNAME TAKEN
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            if password == confirm_password:
                password_hash = hash_pw(password)
                add_account(username, password_hash, 1)
                return redirect(url_for('login'))
        except KeyError:
            pass
        flash("Passwords did not match! Please try again.", 'alert-danger')
    return render_template('signup.html')


@app.route("/home", methods=['GET'])
def home():
    username=request.args.get('username')
    access_lvl = request.args.get('access_lvl')
    flash("Welcome, " + username + "! You have logged in!", "alert-success")
    return render_template('home.html', username=username, access_lvl=access_lvl)
