import flask_login
import base64

from . import login_manager

class User(flask_login.UserMixin):
    pass

@login_manager.request_loader
def load_user_from_request(request):

    if request.headers.get('Auth-User'):
        user = User()
        user.id = request.headers.get('Auth-User')
        user.name = request.headers.get('Name')
        user.email = request.headers.get('Email')
        return user
    else:
        return None
