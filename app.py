from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder="instance/static")


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')
