from flask import render_template, request, jsonify
from app.main import bp
from app.models import Product
from flask_login import current_user
from app import db

@bp.route('/')
@bp.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(
        page=page, per_page=12, error_out=False
    )
    return render_template('index.html', products=products, current_user=current_user)

@bp.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product, current_user=current_user)

@bp.route('/search')
def search():
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    
    products_query = Product.query
    
    if query:
        products_query = products_query.filter(
            Product.name.ilike(f'%{query}%') | 
            Product.description.ilike(f'%{query}%')
        )
    
    if category:
        products_query = products_query.filter_by(category=category)
    
    page = request.args.get('page', 1, type=int)
    products = products_query.paginate(
        page=page, per_page=12, error_out=False
    )
    
    return render_template('search.html', products=products, query=query, category=category, current_user=current_user)

@bp.route('/categories')
def categories():
    categories = db.session.query(Product.category).distinct().all()
    categories = [cat[0] for cat in categories if cat[0]]
    return render_template('categories.html', categories=categories, current_user=current_user)

@bp.route('/category/<category>')
def category_products(category):
    page = request.args.get('page', 1, type=int)
    products = Product.query.filter_by(category=category).paginate(
        page=page, per_page=12, error_out=False
    )
    return render_template('category.html', products=products, category=category, current_user=current_user)