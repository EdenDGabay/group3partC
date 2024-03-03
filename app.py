from flask import Flask, redirect, url_for, render_template
from pages.HomePage.HomePage import HomePage
from pages.Login.Login import Login
from pages.SignUp.SignUp import SignUp
from pages.Categories.Categories import Categories

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(HomePage)
app.register_blueprint(Login, url_prefix='/login')
app.register_blueprint(SignUp, url_prefix='/signup')
app.register_blueprint(Categories, url_prefix='/categories')

@app.route('/')
def home():
    # Redirect to the homepage Blueprint
    return redirect('/homepage')

if __name__ == '__main__':
    app.run(debug=True)