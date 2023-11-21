from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return "Hello World!"


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')
