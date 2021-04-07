from flask import Blueprint

auth = Blueprint('auth', __name__)

# define login route
@auth.route('/login')
def login():
    return "LOGIN"

# define logout route
@auth.route('/logout')
def logout():
    return "THIS IS LOGOUT"
    
#define register route
@auth.route('/register')
def register():
    return "THIS IS REGISTER"