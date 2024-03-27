from flask import Blueprint, render_template
from flask import request, redirect, url_for
from utilities.db.mongo_util import mongo_db_instance

SignUp = Blueprint('SignUp',
                   __name__,
                   static_folder='static',
                   static_url_path='/SignUp',
                   template_folder='templates')

@SignUp.route('/')
def signup():
    return render_template('SignUp.html')


@SignUp.route('/', methods=['POST'])
def signup_post():
    # Get form details
    email = request.form.get('email')
    password = request.form.get('password')
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    birthdate = request.form.get('birthdate')


    # Check if user already exists
    db = mongo_db_instance()
    users_collection = db['Users']
    existing_user = users_collection.find_one( {'email': email} )
    if existing_user:
        # User already exists, redirect to error page or display error message
        return render_template('SignUp.html', error_message='E-Mail already taken')

    # Validate form details
    if not email or not password or not firstName or not lastName or not birthdate:
        # Missing form details, redirect to error page or display error message
        return render_template('SignUp.html', error_message='Please fill in all the required fields')

    # Create new user
    new_user = {
        'email': email,
        'password': password,
        'firstName': firstName,
        'lastName': lastName,
        'birthdate': birthdate
    }
    users_collection.insert_one(new_user)
    print("here")


    # Redirect to login page
    return redirect(url_for('Login.login', msg = "User created successfully! Please login."))

