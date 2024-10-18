from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    reviews = db.relationship('Review', back_populates='user')

class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200))
    instructions = db.Column(db.Text)
    glass_type = db.Column(db.String(50))
    ingredients = db.relationship('CocktailIngredient', back_populates='cocktail')
    reviews = db.relationship('Review', back_populates='cocktail')

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    cocktails = db.relationship('CocktailIngredient', back_populates='ingredient')

class CocktailIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    amount = db.Column(db.String(50))
    cocktail = db.relationship('Cocktail', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='cocktails')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id'), nullable=False)
    user = db.relationship('User', back_populates='reviews')
    cocktail = db.relationship('Cocktail', back_populates='reviews')