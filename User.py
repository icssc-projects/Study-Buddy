from db import db

class User(db.Model):
    __tablename__ = "User"

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.NVARCHAR(11))
    email = db.Column(db.NVARCHAR(40))
    bio = db.Column(db.NVARCHAR(1000), default = None)
