from flask import Flask, Blueprint, request
from .settings import SITE_PATH
import sqlite3

# Use Blueprints to automatically use the app subfolder
bp = Blueprint('main', __name__, url_prefix=SITE_PATH)

# Define your routes
@bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Exemple of SSO use
@bp.route("/user")
def user():
    if request.headers.get('Auth-User'):
        id = request.headers.get('Auth-User')
        name = request.headers.get('Name')
        email = request.headers.get('Email')

        return f'<p>Hello, {name}! Your ID is {id} and e-mail is {email}.</p>'
    else:
        return "<p>Hello, Anonymous!</p>"
    
# Example to use SQLite
@bp.route("/sqlite")
def sqlite():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE movie(title, year, score)")
    finally:
        res = cur.execute("SELECT name FROM sqlite_master")
        data = res.fetchone()
        return str(data)

# After defining all routes, create Flask app and register Blueprint.
app = Flask(__name__)
app.register_blueprint(bp)