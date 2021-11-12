from flask import Flask, Blueprint, jsonify, render_template, flash, redirect, request, url_for
from .settings import *
from .models import User
from flask_login import current_user, login_required

main = Blueprint('main', __name__, url_prefix=SITE_ROOT)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/hello_world')
def hello_world():
    return 'Hello, World!'

@main.route('/protected')
@login_required
def protected():
    return 'Hello, World!'

@main.route('/users')
def users():
    return jsonify([ (u.username, u.email) for u in User.query.all() ])


