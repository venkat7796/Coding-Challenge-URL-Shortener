from db import db

class urlModel(db.Model):
    __tablename__ = "urlmap"
    id = db.Column(db.Integer,primary_key=True)
    longUrl = db.Column(db.String(256),nullable=False,unique=True)
    shortUrl = db.Column(db.String(256),nullable=False,unique=True)
    shortUrlId = db.Column(db.String(256),nullable=False,unique=True)