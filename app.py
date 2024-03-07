from flask import Flask, redirect, url_for, render_template
from pages.HomePage.HomePage import HomePage
from pages.Login.Login import Login
from pages.SignUp.SignUp import SignUp
from pages.Categories.Categories import Categories

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# Register Blueprints
app.register_blueprint(HomePage)
app.register_blueprint(Login, url_prefix='/login')
app.register_blueprint(SignUp, url_prefix='/signup')
app.register_blueprint(Categories, url_prefix='/categories')

@app.route('/')
def home():
    categories = [
        {'name': 'Mystery', 'filename': 'MysteryCategory.jpg'},
        {'name': 'Fantasy', 'filename': 'FantasyCategory.jpg'},
        {'name': 'Biography', 'filename': 'BiographyCategory.jpg'},
        {'name': 'Horror', 'filename': 'HorrorCategory.jpg'},
        {'name': 'Romance', 'filename': 'RomanceCategory.jpeg'},
        {'name': 'Comedy', 'filename': 'ComedyCategory.jpg'},
        {'name': 'Adventure', 'filename': 'AdventureCategory.jpg'},
        {'name': 'Science Fiction', 'filename': 'ScienceFictionCategory.jpg'},
        {'name': 'History', 'filename': 'HistoryCategory.png'},
    ]
    return render_template('HomePage.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)