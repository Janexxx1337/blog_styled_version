from flask import Flask, render_template,request
import requests
import datetime
import smtplib

my_email = 'vova@infomxxwedspb.ru'
my_password = 'xffwqizdxsyuxwcxcxnr'

app = Flask(__name__)


@app.route('/')
def home():
    current_date = datetime.date.today()
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    return render_template("index.html", post=response, date=current_date)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        msg = data["message"]
        connection = smtplib.SMTP('smtp.yandex.com')
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="krahs123@gmail.com",
            msg=f'Имя: {name}\n Почта: {email}\n Телефон: {phone}\n Сообщение: {msg}'.encode('utf-8').strip())
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



@app.route('/post/<num>')
def get_page(num):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    return render_template("post.html", post=response, num=int(num))



app.run(debug=True)