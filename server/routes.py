from flask import Blueprint, request, jsonify
from models import User, Cocktail, Ingredient, CocktailIngredient, Review
from extensions import db

api_bp = Blueprint('api', __name__)

# Create a User
@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email}), 201

# Get all Users
@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

# Create a Cocktail
@api_bp.route('/cocktails', methods=['POST'])
def create_cocktail():
    data = request.get_json()
    new_cocktail = Cocktail(
        name=data['name'],
        image_url=data.get('image_url'),
        instructions=data.get('instructions'),
        glass_type=data.get('glass_type')
    )
    db.session.add(new_cocktail)
    db.session.commit()
    return jsonify({'id': new_cocktail.id, 'name': new_cocktail.name}), 201

# Get all Cocktails
@api_bp.route('/cocktails', methods=['GET'])
def get_cocktails():
    cocktails = Cocktail.query.all()
    return jsonify([{
        'id': cocktail.id,
        'name': cocktail.name,
        'image_url': cocktail.image_url,
        'instructions': cocktail.instructions,
        'glass_type': cocktail.glass_type
    } for cocktail in cocktails])

# Create a Review
@api_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    new_review = Review(
        content=data['content'],
        rating=data['rating'],
        user_id=data['user_id'],
        cocktail_id=data['cocktail_id']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'id': new_review.id, 'content': new_review.content, 'rating': new_review.rating}), 201

# Get all Reviews for a specific Cocktail
@api_bp.route('/cocktails/<int:cocktail_id>/reviews', methods=['GET'])
def get_reviews_for_cocktail(cocktail_id):
    reviews = Review.query.filter_by(cocktail_id=cocktail_id).all()
    return jsonify([{
        'id': review.id,
        'content': review.content,
        'rating': review.rating,
        'user_id': review.user_id
    } for review in reviews])

# Update a Cocktail
@api_bp.route('/cocktails/<int:id>', methods=['PUT'])
def update_cocktail(id):
    data = request.get_json()
    cocktail = Cocktail.query.get_or_404(id)
    cocktail.name = data.get('name', cocktail.name)
    cocktail.image_url = data.get('image_url', cocktail.image_url)
    cocktail.instructions = data.get('instructions', cocktail.instructions)
    cocktail.glass_type = data.get('glass_type', cocktail.glass_type)
    db.session.commit()
    return jsonify({'id': cocktail.id, 'name': cocktail.name}), 200

# Delete a Cocktail
@api_bp.route('/cocktails/<int:id>', methods=['DELETE'])
def delete_cocktail(id):
    cocktail = Cocktail.query.get_or_404(id)
    db.session.delete(cocktail)
    db.session.commit()
    return jsonify({'message': 'Cocktail deleted successfully'}), 200
