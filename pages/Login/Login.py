from flask import Blueprint, render_template, request, redirect

Login = Blueprint('Login',
                  __name__,
                  static_folder='static',
                  static_url_path='/Login',
                  template_folder='templates'
                  )


@Login.route('/login')
def login():
    return render_template('Login.html')