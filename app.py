from flask import Flask, render_template, redirect, request
from intranetLogin import authenticate

app = Flask(__name__, static_folder="instance/static")


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        accessLvl = authenticate("intranetInfo.csv", user, password)
        if accessLvl != -1:
            return "Hey, " + user + ", welcome! Your access level is " + str(accessLvl)
        else:
            return render_template('home.html')

    return render_template('home.html')


