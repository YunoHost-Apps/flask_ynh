from flask import Flask, Blueprint
from .settings import *

main = Blueprint('main', __name__, url_prefix=SITE_ROOT)


@main.route('/')
def hello_world():
    return 'Hello, World!'
