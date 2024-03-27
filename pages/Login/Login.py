from flask import Blueprint, render_template
from flask import request, session, redirect, url_for
from flask import current_app
from pymongo import MongoClient
from utilities.db.mongo_util import mongo_db_instance

Login = Blueprint('Login',
                  __name__,
                  static_folder='static',
                  static_url_path='/Login',  # This sets the URL path for static files, not for routes
                  template_folder='templates')

@Login.route('/')
def login():
    args = request.args
    msg = args.get('msg', default="", type=str)
    return render_template('Login.html', msg  = msg)

@Login.route('/', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if username and password are provided
    if not email or not password:
        error_message = 'Please provide both email and password.'
        return render_template('Login.html', error_message=error_message)

    # Check if username and password match in the Users collection

    # Get Users collection
    db = mongo_db_instance()
    users_collection = db['Users']
    user = users_collection.find_one({'email': email, 'password': password})
    if user:
        # Set session cookie and redirect to homepage
        session['username'] = user["firstName"]
        return redirect(url_for('HomePage.index'))
    else:
        error_message = 'Invalid username or password.'
        return render_template('Login.html', error_message=error_message)