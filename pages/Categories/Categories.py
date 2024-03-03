from flask import Blueprint, render_template

Categories = Blueprint('Categories',
                       __name__,
                       static_folder='static',
                       static_url_path='/categories',
                       template_folder='templates')

# Route for the categories overview (if needed)
@Categories.route('/')
def categories_overview():
    # Here you would pass the categories to your template.
    # The actual categories data should eventually come from your database
    # For now, you can pass an empty list or some placeholder data
    return render_template('Categories.html', categories=[])

# Route for individual categories
@Categories.route('/<category_name>')  # This matches '/categories/<category_name>'
def category(category_name):
    # Placeholder for category-specific data
    # This data will also come from your database in the future
    return render_template('Category.html', category_name=category_name, books=[])
