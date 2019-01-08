from flask import Flask, render_template, url_for
from connection import connect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("base.html")


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/active-users')
def users():
    try:
        cursor, connection = connect()
        ### Execute the query, then obtain the data from the cursor
        cursor.execute("""select * from User""")
        users = cursor.fetchall()
        return render_template("users.html", users = str(users))
    except Exception as e:
        ### If an error occurs, this will return the error as a string
        return str(e)


# sudo mysql -u roots
