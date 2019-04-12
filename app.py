from flask import Flask, render_template, url_for, request, redirect
from connection import connect
from flask_sqlalchemy import SQLAlchemy
from db import db
from User import User
from Post import Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://fVb9YnCgUU:L7AZ3KCccR@remotemysql.com/fVb9YnCgUU'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

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

@app.route('/courses')
def courses():
    return render_template("courses.html")




@app.route('/create-account')
def createAccount():
    try:
        ## Use the cursor to insert into User
        ## Set session variable to logged_in = True, username = ****, uid - ###
        ## Use these values throughout the session
        ## Session variables can be accessed in HTML files without passing them

        return render_template("create-account.html")
    except Exception as e:
        return str(e)

@app.route('/posts')
def posts():
    try:
        cursor, connection = connect()
        cursor.execute("""select * from Post""")
        posts = cursor.fetchall()
        connection.close()
        cursor.close()
        #posts = Post.query.order_by(Post.post_id).all()
        return render_template("posts.html", posts = posts, size = len(posts))
    except Exception as e:
        return str(e)

# INSERT INTO `Post` (`post_id`, `user_id`, `username`, `title`, `text`, `course`) 
# VALUES (NULL, '1', 'wrcastel', 'Looking for a buddy', 'Does anybody want to study at Ayala tonight at 4pm?', 'CS143B')


@app.route('/create-post',  methods = ['GET', 'POST'])
def createPost():
    try:
        ## Use the cursor to insert into Post
        ## Make sure to insert the current session's username and uid
        if request.method == "POST":
            title = request.form['title']
            text = request.form['text']
            course = request.form['course']
            #return str([title, text, course])

            # These lines need to be replaced based on the user current logged in session
            username = "wrcastel"
            user_id = 1
            ##############
            cursor, connection = connect()
            cursor.execute('insert into Post(user_id, username, title, text, course)\
                            values("%d", "%s", "%s", "%s", "%s")' \
                            % (1, "wrcastel", title, text, course))
            connection.commit()
            return redirect(url_for('posts'))
        return render_template("create-post.html")
    except Exception as e:
        return str(e)


# The information is accessible now. Post and User are the main objects.


