from flask import Blueprint, render_template, session
from flask import request, redirect, url_for
from utilities.db.mongo_util import mongo_db_instance
from bson.objectid import ObjectId

EditBook = Blueprint('EditBook',
                   __name__,
                   static_folder='static',
                   static_url_path='/EditBook',
                   template_folder='templates')

@EditBook.route('/')
def AddBook():
    db = mongo_db_instance()
    categories_collection = db['Categories']
    categories = categories_collection.find()
    return render_template('EditBook.html', categories=categories)

@EditBook.route('/<book_id>')
def EditBook_get(book_id):
    if session.get('username'):
        db = mongo_db_instance()
        books_collection = db['Books']
        print(book_id)
        book = books_collection.find_one({'_id': ObjectId(book_id)})
        print(book)
        categories_collection = db['Categories']
        categories = categories_collection.find()
        if not book:
            return render_template('EditBook.html', categories=categories, error_message="Invalid Book ID", is_edit=True)
        return render_template('EditBook.html', categories=categories, book=book, is_edit=True)
    return redirect(url_for('Login.login'))



@EditBook.route('/', methods=['POST'])
def AddBook_Post():
    if session.get('username'):
        db = mongo_db_instance()
        book = {
                    'title': request.form.get('title'),
                    'author': request.form.get('author'),
                    'category': request.form.get('category'),
                    'details': request.form.get('details'),
                    'imageSrc': request.form.get('imageSrc')
                    }
        books_collection = db['Books']
        categories_collection = db['Categories']
        categories = categories_collection.find()
        # Validate the fields
        if 'title' in request.form and 'author' in request.form and 'category' in request.form and 'details' in request.form and 'imageSrc' in request.form:
            category = request.form['category']
            if categories_collection.find_one({'name': category}):
                imageSrc = request.form['imageSrc']
                if imageSrc.startswith('http://') or imageSrc.startswith('https://'):
                    # Fields are valid, continue with adding the book
                    
                    books_collection.insert_one(book)
                    return redirect(url_for('Category.category', category_name=category, msg = "Book added successfully!"))
                else:
                    return render_template('EditBook.html', book=book, categories=categories, error_message="Invalid Image URL")
            else:
                return render_template('EditBook.html', book=book, categories=categories, error_message="Invalid Category")
        else:
            return render_template('EditBook.html', book=book, categories=categories, error_message="Please fill all fields")
    return redirect(url_for('Login.login'))

@EditBook.route('/<book_id>', methods=['POST'])
def EditBook_Post(book_id):
    db = mongo_db_instance()
    books_collection = db['Books']
    categories_collection = db['Categories']
    categories = categories_collection.find()
    book = books_collection.find_one({'_id': ObjectId(book_id)})
    if not book:
        return render_template('EditBook.html', categories=categories, error_message="Invalid Book ID")
    print(request.form)

    book = {
                    'title': request.form.get('title'),
                    'author': request.form.get('author'),
                    'category': request.form.get('category'),
                    'details': request.form.get('details'),
                    'imageSrc': request.form.get('imageSrc')
                }
    # Validate the fields
    if 'title' in request.form and 'author' in request.form and 'category' in request.form and 'details' in request.form and 'imageSrc' in request.form:
        category = request.form['category']
        if categories_collection.find_one({'name': category}):
            imageSrc = request.form['imageSrc']
            if imageSrc.startswith('http://') or imageSrc.startswith('https://'):
                books_collection.update_one({'_id': ObjectId(book_id)}, {'$set': book})
                return redirect(url_for('Category.category', category_name=category, msg = "Book edited successfully!"))
            else:
                return render_template('EditBook.html', categories=categories, book=book, error_message="Invalid Image URL", is_edit=True)
        else:
            return render_template('EditBook.html', categories=categories, book=book, error_message="Invalid Category",  is_edit=True)
    else:
        return render_template('EditBook.html', categories=categories, book=book, error_message="Please fill all fields", is_edit=True)
        
