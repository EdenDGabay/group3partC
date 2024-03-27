from flask import Blueprint, render_template, request
from utilities.db.mongo_util import mongo_db_instance
import re
Search = Blueprint('Search',
                       __name__,
                       static_folder='static',
                       static_url_path='/Search',
                       template_folder='templates')


# Route for individual categories
@Search.route('/')  # This matches '/categories/<category_name>'
def search():
    search_term = request.args.get('search_term')
    # Placeholder for category-specific data
    db = mongo_db_instance()
    books = db['Books']
    books = books.find({'$or': [{'title': {'$regex': search_term, '$options': 'i'}}, {'details': {'$regex': search_term, '$options': 'i'}}]})
    books = [book for book in books]
    if len(books)==0:
        return render_template('Search.html', search_term=search_term, error_message="No books found")
    return render_template('Search.html', search_term=search_term, books=books)

