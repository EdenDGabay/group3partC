from flask import Blueprint, render_template, session
from flask import request, redirect, url_for
from utilities.db.mongo_util import mongo_db_instance
from bson.objectid import ObjectId

RemoveBook = Blueprint('RemoveBook',
                   __name__,
                   static_folder='static',
                   static_url_path='/RemoveBook',
                   template_folder='templates')


@RemoveBook.route('/<book_id>')
def remove_book(book_id):
    if session.get('username'):
        db = mongo_db_instance()
        books_collection = db['Books']
        book = books_collection.find_one({'_id': ObjectId(book_id)})
        if book:
            category = book.get('category')
            books_collection.delete_one({'_id': ObjectId(book_id)})
            return redirect(url_for('Category.category', category_name=category, msg = "Book deleted successfully!"))
        return redirect(url_for('HomePage.index'))
    return redirect(url_for('Login.login'))


