from flask import Blueprint, render_template, url_for

from utilities.db.mongo_util import mongo_db_instance

HomePage = Blueprint('HomePage',
                     __name__,
                     static_folder='static',
                     static_url_path='/HomePage',
                     template_folder='templates')

# Static data to simulate database entries
books_by_category = {
    # ... Your categories and books as before
}

@HomePage.route('/')
def index():
    # The index function will render the homepage template
    db = mongo_db_instance()
    categories = db['Categories']
    categories = categories.find()
    return render_template('HomePage.html', categories=categories)


# You can add more routes for other functionalities here...

# Example book data structure to replace the placeholder
# Add the actual books you want to display in each category
books_by_category = {
    "Mystery": [
        {"title": "The Da Vinci Code", "author": "Dan Brown", "imageSrc": "pictures/DaVinciCode.jpg"},
        # ... other books
    ],
    "Fantasy": [
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "imageSrc": "pictures/HPSorcerereStone.jpg"},
        # ... other books
    ],
    # ... other categories
}

# Ensure to register your Blueprint in the main app
# app.register_blueprint(HomePage, url_prefix='/')
