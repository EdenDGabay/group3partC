from flask import Flask, redirect, url_for, render_template
from pages.EditBook.EditBook import EditBook
from pages.HomePage.HomePage import HomePage
from pages.Login.Login import Login
from pages.Logout.LogOut import LogOut
from pages.RemoveBook.RemoveBook import RemoveBook
from pages.Search.Search import Search
from pages.SignUp.SignUp import SignUp
from pages.Category.Category import Category

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# Register Blueprints
app.register_blueprint(HomePage)
app.register_blueprint(Login, url_prefix='/login')
app.register_blueprint(LogOut, url_prefix='/logout')
app.register_blueprint(SignUp, url_prefix='/signup')
app.register_blueprint(Category, url_prefix='/category')
app.register_blueprint(Search, url_prefix='/search')
app.register_blueprint(EditBook, url_prefix='/edit_book')
app.register_blueprint(RemoveBook, url_prefix='/remove_book')


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)