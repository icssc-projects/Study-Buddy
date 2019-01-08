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



@app.route('/create-account')
def createAccount():
    try:
        ## Use the cursor to insert into User
        ## Set session variable to logged_in = True, username = ****, uid - ###
        ## Use these values throughout the session
        ## Session variables can be accessed in HTML files without passing them
        return render_template("create-user.html")
    except Exception as e:
        return str(e)

@app.route('/posts')
def posts():
    try:
        cursor, connection = connect()
        cursor.execute("""select * from Post""")
        posts = cursor.fetchall()
        return render_template("posts.html", posts = str(posts))
    except Exception as e:
        return str(e)

@app.route('/create-post')
def createPost():
    try:
        ## Use the cursor to insert into Post
        ## Make sure to insert the current session's username and uid
        return render_template("create-post.html")
    except Exception as e:
        return str(e)


# The information is accessible now. Post and User are the main objects.


