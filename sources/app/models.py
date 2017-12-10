from flask_sqlalchemy import SQLAlchemy

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def fake_feed():
        admin = User(username='admin', email='admin@example.com')
        guest = User(username='guest', email='guest@example.com')
        db.session.add(admin)
        db.session.add(guest)
        db.session.commit()

