from flask import Flask, Blueprint, request

# Use Blueprints to automatically use the app subfolder
bp = Blueprint('main', __name__, url_prefix='__PATH__')

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

# After defining all routes, create Flask app and register Blueprint.
app = Flask(__name__)
app.register_blueprint(bp)