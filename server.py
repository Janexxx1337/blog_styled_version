from flask import Flask, render_template
import requests
import datetime


app = Flask(__name__)


@app.route('/')
def home():
    current_date = datetime.date.today()
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    return render_template("index.html", post=response, date=current_date)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/post/<num>')
def get_page(num):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    return render_template("post.html", post=response, num=int(num))

app.run(debug=True)