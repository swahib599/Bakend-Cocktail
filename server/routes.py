from flask import jsonify, request, abort
from app import app, db
from models import Cocktail, Ingredient, CocktailIngredient, Review, User

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Cocktail API"})

@app.route('/api/cocktails', methods=['GET'])
def get_cocktails():
    cocktails = Cocktail.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'image_url': c.image_url,
        'instructions': c.instructions,
        'glass_type': c.glass_type,
        'ingredients': [{
            'name': ci.ingredient.name,
            'amount': ci.amount
        } for ci in c.ingredients]
    } for c in cocktails])

@app.route('/api/cocktails/<int:id>', methods=['GET'])
def get_cocktail(id):
    cocktail = Cocktail.query.get_or_404(id)
    return jsonify({
        'id': cocktail.id,
        'name': cocktail.name,
        'image_url': cocktail.image_url,
        'instructions': cocktail.instructions,
        'glass_type': cocktail.glass_type,
        'ingredients': [{
            'name': ci.ingredient.name,
            'amount': ci.amount
        } for ci in cocktail.ingredients],
        'reviews': [{
            'id': r.id,
            'content': r.content,
            'rating': r.rating,
            'user': r.user.username
        } for r in cocktail.reviews]
    })

@app.route('/api/cocktails/<int:id>/reviews', methods=['GET'])
def get_cocktail_reviews(id):
    cocktail = Cocktail.query.get_or_404(id)
    return jsonify([{
        'id': r.id,
        'content': r.content,
        'rating': r.rating,
        'user': r.user.username
    } for r in cocktail.reviews])

@app.route('/api/cocktails/<int:id>/reviews', methods=['POST'])
def add_review(id):
    data = request.json
    cocktail = Cocktail.query.get_or_404(id)
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        user = User(username=data['username'], email=f"{data['username']}@example.com")
        db.session.add(user)
    
    review = Review(
        content=data['content'],
        rating=data['rating'],
        user=user,
        cocktail=cocktail
    )
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully', 'id': review.id}), 201

@app.route('/api/reviews/<int:id>', methods=['PUT'])
def update_review(id):
    review = Review.query.get_or_404(id)
    data = request.json
    
    if 'content' in data:
        review.content = data['content']
    if 'rating' in data:
        review.rating = data['rating']
    
    db.session.commit()
    return jsonify({'message': 'Review updated successfully'})

@app.route('/api/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'})

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully', 'id': user.id}), 201

@app.route('/api/users/<int:id>/reviews', methods=['GET'])
def get_user_reviews(id):
    user = User.query.get_or_404(id)
    return jsonify([{
        'id': r.id,
        'content': r.content,
        'rating': r.rating,
        'cocktail': r.cocktail.name
    } for r in user.reviews])

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'message': 'Bad request'}), 400

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message': 'Internal server error'}), 500