from flask import Flask, Blueprint, jsonify
from .settings import *
from .models import User

main = Blueprint('main', __name__, url_prefix=SITE_ROOT)

@main.route('/')
def hello_world():
    return 'Hello, World!'


@main.route('/users')
def users():
    return jsonify([ (u.username, u.email) for u in User.query.all() ])


