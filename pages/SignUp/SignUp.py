from flask import Blueprint, render_template

SignUp = Blueprint('SignUp',
                   __name__,
                   static_folder='static',
                   static_url_path='/SignUp',
                   template_folder='templates')

@SignUp.route('/')
def signup():
    return render_template('SignUp.html')
