from db import db

class Post(db.Model):
    __tablename__ = "Post"
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    post_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.VARCHAR(30))
    text = db.Column(db.VARCHAR(30))
    course = db.Column(db.VARCHAR(20))