from app import app, db
from models import User, Cocktail, Ingredient, CocktailIngredient, Review

def seed_data():
    # Create sample users
    user1 = User(username='johndoe', email='john@example.com')
    user2 = User(username='janedoe', email='jane@example.com')

    db.session.add_all([user1, user2])

    # Create sample cocktails
    cocktail1 = Cocktail(
        name='Mojito',
        image_url='https://example.com/mojito.jpg',
        instructions='Mix mint leaves with sugar, add lime juice, rum, and soda water.',
        glass_type='Highball glass'
    )
    cocktail2 = Cocktail(
        name='Margarita',
        image_url='https://example.com/margarita.jpg',
        instructions='Shake tequila, lime juice, and triple sec with ice. Strain into a glass.',
        glass_type='Cocktail glass'
    )

    db.session.add_all([cocktail1, cocktail2])

    # Create sample ingredients
    ingredient1 = Ingredient(name='Mint Leaves')
    ingredient2 = Ingredient(name='Sugar')
    ingredient3 = Ingredient(name='Lime Juice')
    ingredient4 = Ingredient(name='Rum')
    ingredient5 = Ingredient(name='Soda Water')
    ingredient6 = Ingredient(name='Tequila')
    ingredient7 = Ingredient(name='Triple Sec')

    db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7])

    # Create sample cocktail ingredients relationships
    cocktail_ingredient1 = CocktailIngredient(cocktail=cocktail1, ingredient=ingredient1, amount='10 leaves')
    cocktail_ingredient2 = CocktailIngredient(cocktail=cocktail1, ingredient=ingredient2, amount='2 teaspoons')
    cocktail_ingredient3 = CocktailIngredient(cocktail=cocktail1, ingredient=ingredient3, amount='30 ml')
    cocktail_ingredient4 = CocktailIngredient(cocktail=cocktail1, ingredient=ingredient4, amount='60 ml')
    cocktail_ingredient5 = CocktailIngredient(cocktail=cocktail1, ingredient=ingredient5, amount='120 ml')
    cocktail_ingredient6 = CocktailIngredient(cocktail=cocktail2, ingredient=ingredient6, amount='50 ml')
    cocktail_ingredient7 = CocktailIngredient(cocktail=cocktail2, ingredient=ingredient3, amount='25 ml')
    cocktail_ingredient8 = CocktailIngredient(cocktail=cocktail2, ingredient=ingredient7, amount='25 ml')

    db.session.add_all([
        cocktail_ingredient1, cocktail_ingredient2, cocktail_ingredient3,
        cocktail_ingredient4, cocktail_ingredient5, cocktail_ingredient6,
        cocktail_ingredient7, cocktail_ingredient8
    ])

    # Create sample reviews
    review1 = Review(content='Refreshing and minty!', rating=5, user=user1, cocktail=cocktail1)
    review2 = Review(content='Perfect balance of sour and sweet.', rating=4, user=user2, cocktail=cocktail2)

    db.session.add_all([review1, review2])

    # Commit all changes to the database
    db.session.commit()
    print('Database seeded successfully!')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the tables are created
        seed_data()  # Populate the database with seed data
