from flask import Blueprint, render_template, request
from utilities.db.mongo_util import mongo_db_instance
import re
Category = Blueprint('Category',
                       __name__,
                       static_folder='static',
                       static_url_path='/Category',
                       template_folder='templates')

# # Route for the categories overview (if needed)
# @Categories.route('/')
# def categories_overview():
#     # Here you would pass the categories to your template.
#     # The actual categories data should eventually come from your database
#     # For now, you can pass an empty list or some placeholder data
#     return render_template('Categories.html', categories=[])

# Route for individual categories
@Category.route('/<category_name>/')  # This matches '/categories/<category_name>'
def category(category_name):
    args = request.args
    msg = args.get('msg', default="", type=str)
    db = mongo_db_instance()
    books = db['Books']
    books = books.find({'category': category_name})
    return render_template('Category.html', category_name=category_name, books=books, msg=msg)

@Category.route('/<category_name>', methods=['POST'])  # This matches '/categories/<category_name>'
def add_book(category_name):
    title = request.form.get('title')
    author = request.form.get('author')
    imageSrc = request.form.get('imageSrc')
    if not title or not author:
        return render_template('Category.html', category_name=category_name, books=books.find({'category': category_name}), error_msg="Title and author fields cannot be empty")

    url_pattern = re.compile(r'^https?://\S+$')
    if not url_pattern.match(imageSrc):
        return render_template('Category.html', category_name=category_name, books=books.find({'category': category_name}), error_msg="Invalid image URL")

    details = request.form.get('details')
    db = mongo_db_instance()
    books = db['Books']
    books.insert_one({'title': title, 'author': author, 'imageSrc': imageSrc, 'details': details, 'category': category_name})
    return render_template('Category.html', category_name=category_name, books=books.find({'category': category_name}))

    

