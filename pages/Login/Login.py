from flask import Blueprint, render_template

Login = Blueprint('Login',
                  __name__,
                  static_folder='static',
                  static_url_path='/Login',  # This sets the URL path for static files, not for routes
                  template_folder='templates')

@Login.route('/')
def login():
    return render_template('Login.html')