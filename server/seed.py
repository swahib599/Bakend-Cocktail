import logging
from app import app, db
from models import User, Cocktail, Ingredient, CocktailIngredient, Review

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_data():
    try:
        logger.info("Starting the seeding process...")

        # Clear existing data
        Cocktail.query.delete()
        Ingredient.query.delete()
        db.session.commit()
        logger.info("Deleted existing cocktails and ingredients.")

        cocktails = [
        # Alcoholic Cocktails
        {
            "name": "Mojito",
            "id": 1,
            "image": "/static/mojito.jpeg",
            "ingredients": [
                "2 oz White Rum",
                "1 oz Fresh Lime Juice",
                "2 tsp Sugar",
                "6-8 Fresh Mint Leaves",
                "Club Soda",
                "Mint Sprig for garnish"
            ],
            "directions": "Muddle mint leaves and sugar with lime juice. Add rum and top with club soda. Garnish with mint sprig.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Margarita",
            "id": 2,
            "image": "/static/margarita.jpeg",
            "ingredients": [
                "2 oz Tequila",
                "1 oz Lime Juice",
                "1 oz Triple Sec",
                "Salt for rimming glass",
                "Lime wedge for garnish"
            ],
            "directions": "Rub the rim of the glass with lime and dip in salt. Shake tequila, lime juice, and triple sec with ice. Strain into glass.",
            "glass_type": "Cocktail Glass"
        },
        {
            "name": "Old Fashioned",
            "id": 3,
            "image": "/static/oldFashioned.jpeg",
            "ingredients": [
                "2 oz Bourbon or Rye Whiskey",
                "1 Sugar Cube",
                "2-3 dashes Angostura Bitters",
                "Orange Twist",
                "Maraschino Cherry for garnish"
            ],
            "directions": "Muddle sugar and bitters. Add whiskey and ice, stir. Garnish with orange twist and cherry.",
            "glass_type": "Old Fashioned Glass"
        },
        {
            "name": "Pina Colada",
            "id": 4,
            "image": "/static/pinaColada.jpeg",
            "ingredients": [
                "2 oz White Rum",
                "1 oz Coconut Cream",
                "1 oz Heavy Cream",
                "6 oz Fresh Pineapple Juice",
                "1/2 cup Crushed Ice",
                "Pineapple wedge for garnish"
            ],
            "directions": "Blend all ingredients until smooth. Serve in a chilled glass with a pineapple wedge.",
            "glass_type": "Hurricane Glass"
        },
        {
            "name": "Cosmopolitan",
            "id": 5,
            "image": "/static/cosmopolitan.jpeg",
            "ingredients": [
                "1 1/2 oz Vodka",
                "1 oz Cranberry Juice",
                "1/2 oz Triple Sec",
                "1/2 oz Fresh Lime Juice",
                "Lime wheel for garnish"
            ],
            "directions": "Shake all ingredients with ice and strain into a chilled cocktail glass. Garnish with lime wheel.",
            "glass_type": "Martini Glass"
        },
        {
            "name": "Daiquiri",
            "id": 6,
            "image": "/static/daiquiri.jpeg",
            "ingredients": [
                "2 oz White Rum",
                "1 oz Lime Juice",
                "3/4 oz Simple Syrup"
            ],
            "directions": "Shake all ingredients with ice and strain into a chilled cocktail glass.",
            "glass_type": "Cocktail Glass"
        },
        {
            "name": "Whiskey Sour",
            "id": 7,
            "image": "/static/whiskey_sour.jpeg",
            "ingredients": [
                "2 oz Whiskey",
                "3/4 oz Lemon Juice",
                "1/2 oz Simple Syrup",
                "Cherry for garnish"
            ],
            "directions": "Shake with ice and strain into a rocks glass. Garnish with cherry.",
            "glass_type": "Rocks Glass"
        },
        {
            "name": "Gin and Tonic",
            "id": 8,
            "image": "/static/gintonic.jpeg",
            "ingredients": [
                "2 oz Gin",
                "4 oz Tonic Water",
                "Lime Wedge"
            ],
            "directions": "Pour gin into a glass filled with ice. Top with tonic water and garnish with lime.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Long Island Iced Tea",
            "id": 9,
            "image": "/static/longisland.jpeg",
            "ingredients": [
                "1/2 oz Vodka",
                "1/2 oz Tequila",
                "1/2 oz Rum",
                "1/2 oz Gin",
                "1/2 oz Triple Sec",
                "1 oz Sour Mix",
                "Coca-Cola to top"
            ],
            "directions": "Mix all spirits and sour mix in a shaker with ice. Strain into a glass and top with cola.",
            "glass_type": "Collins Glass"
        },
        {
            "name": "Bellini",
            "id": 10,
            "image": "/static/bellini.jpeg",
            "ingredients": [
                "1 oz Peach Puree",
                "4 oz Prosecco"
            ],
            "directions": "Pour peach puree into a champagne flute and top with prosecco. Stir gently.",
            "glass_type": "Champagne Flute"
        },
        {
            "name": "Mai Tai",
            "id": 11,
            "image": "/static/maitai.jpeg",
            "ingredients": [
                "1 oz Light Rum",
                "1 oz Dark Rum",
                "1/2 oz Orange Curacao",
                "1/2 oz Orgeat Syrup",
                "1/2 oz Fresh Lime Juice"
            ],
            "directions": "Shake with ice and strain into a glass filled with crushed ice.",
            "glass_type": "Old Fashioned Glass"
        },
        {
            "name": "Sangria",
            "id": 12,
            "image": "/static/sangria.jpeg",
            "ingredients": [
                "1 bottle Red Wine",
                "1/4 cup Brandy",
                "1/4 cup Orange Juice",
                "Sliced Fruits"
            ],
            "directions": "Mix all ingredients in a pitcher and chill before serving.",
            "glass_type": "Wine Glass"
        },
        {
            "name": "Aperol Spritz",
            "id": 13,
            "image": "/static/aperolspritz.jpeg",
            "ingredients": [
                "3 oz Prosecco",
                "2 oz Aperol",
                "1 oz Soda Water",
                "Orange Slice for garnish"
            ],
            "directions": "Combine ingredients in a glass with ice and garnish with an orange slice.",
            "glass_type": "Wine Glass"
        },
        {
            "name": "Negroni",
            "id": 14,
            "image": "/static/negroni.jpeg",
            "ingredients": [
                "1 oz Gin",
                "1 oz Campari",
                "1 oz Sweet Vermouth"
            ],
            "directions": "Stir ingredients with ice and strain into a rocks glass.",
            "glass_type": "Rocks Glass"
        },
        {
            "name": "Vesper Martini",
            "id": 15,
            "image": "/static/vespermartini.jpeg",
            "ingredients": [
                "3 oz Gin",
                "1 oz Vodka",
                "1/2 oz Lillet Blanc"
            ],
            "directions": "Shake with ice and strain into a chilled martini glass.",
            "glass_type": "Martini Glass"
        },
        {
            "name": "French 75",
            "id": 16,
            "image": "/static/french75.jpeg",
            "ingredients": [
                "1 oz Gin",
                "1 oz Lemon Juice",
                "2 oz Champagne"
            ],
            "directions": "Shake gin and lemon juice with ice, strain into flute, and top with champagne.",
            "glass_type": "Champagne Flute"
        },
        {
            "name": "Rum Punch",
            "id": 17,
            "image": "/static/rumpunch.jpeg",
            "ingredients": [
                "1 oz Light Rum",
                "1 oz Dark Rum",
                "2 oz Pineapple Juice",
                "1 oz Orange Juice"
            ],
            "directions": "Mix all ingredients and serve over ice.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Tequila Sunrise",
            "id": 18,
            "image": "/static/tequilasunrise.jpeg",
            "ingredients": [
                "2 oz Tequila",
                "4 oz Orange Juice",
                "1/2 oz Grenadine"
            ],
            "directions": "Pour tequila and orange juice into a glass with ice. Slowly add grenadine.",
            "glass_type": "Highball Glass"
        },
        # Non-Alcoholic Cocktails
        {
            "name": "Virgin Mojito",
            "id": 19,
            "image": "/static/virginmojito.jpeg",
            "ingredients": [
                "1 oz Fresh Lime Juice",
                "2 tsp Sugar",
                "6-8 Fresh Mint Leaves",
                "Club Soda",
                "Mint Sprig for garnish"
            ],
            "directions": "Muddle mint leaves and sugar with lime juice. Top with club soda. Garnish with mint sprig.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Shirley Temple",
            "id": 20,
            "image": "/static/shirleytemple.jpeg",
            "ingredients": [
                "1/2 oz Grenadine",
                "1 oz Orange Juice",
                "Ginger Ale",
                "Maraschino Cherry for garnish"
            ],
            "directions": "Pour grenadine and orange juice into a glass filled with ice. Top with ginger ale and garnish.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Nojito",
            "id": 21,
            "image": "/static/nojito.jpeg",
            "ingredients": [
                "1 oz Fresh Lime Juice",
                "2 tsp Sugar",
                "6-8 Fresh Mint Leaves",
                "Club Soda"
            ],
            "directions": "Muddle mint leaves and sugar with lime juice. Top with club soda.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Fruit Punch",
            "id":22,
            "image": "/static/fruitpunch.jpeg",
            "ingredients": [
                "1 cup Mixed Fruit Juice",
                "1/2 cup Club Soda",
                "Sliced Fruits for garnish"
            ],
            "directions": "Mix all ingredients in a pitcher and serve over ice.",
            "glass_type": "Punch Glass"
        },
        {
            "name": "Lemonade",
            "id": 23,
            "image": "/static/lemonade.jpeg",
            "ingredients": [
                "1 cup Fresh Lemon Juice",
                "1 cup Sugar",
                "4 cups Water"
            ],
            "directions": "Mix all ingredients until sugar dissolves. Serve over ice.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Coconut Water Cooler",
            "id": 24,
           "image": "/static/coconutcooler.jpeg",
            "ingredients": [
                "1 cup Coconut Water",
                "1 oz Lime Juice",
                "Mint Leaves for garnish"
            ],
            "directions": "Mix coconut water and lime juice. Garnish with mint leaves.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Virgin Piña Colada",
            "id": 25,
            "image": "/static/virginpcolada.jpeg",
            "ingredients": [
                "1 cup Pineapple Juice",
                "1/2 cup Coconut Cream",
                "1 cup Crushed Ice"
            ],
            "directions": "Blend all ingredients until smooth. Serve in a chilled glass.",
            "glass_type": "Hurricane Glass"
        },
        {
            "name": "Berry Fizz",
            "id": 26,
            "image": "/static/berryfizz.jpeg",
            "ingredients": [
                "1/2 cup Mixed Berries",
                "1 oz Lime Juice",
                "Club Soda"
            ],
            "directions": "Muddle berries and lime juice in a glass. Top with club soda.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Sparkling Apple Cider",
            "id": 27,
            "image": "/static/applecider.jpeg",
            "ingredients": [
                "1 cup Apple Cider",
                "Sparkling Water"
            ],
            "directions": "Mix apple cider with sparkling water. Serve chilled.",
            "glass_type": "Highball Glass"
        },
        {
            "name": "Cucumber Cooler",
            "id": 28,
            "image": "/static/cucumbercooler.jpeg",
            "ingredients": [
                "1/2 cup Cucumber Juice",
                "1 oz Lime Juice",
                "Club Soda"
            ],
            "directions": "Mix cucumber juice and lime juice. Top with club soda.",
            "glass_type": "Highball Glass"
        }
    ]

        for cocktail_data in cocktails:
            # Create Cocktail
            cocktail = Cocktail(
                id=cocktail_data['id'],
                name=cocktail_data['name'],
                image_url=cocktail_data['image'],
                instructions=cocktail_data['directions'],
                glass_type=cocktail_data['glass_type']
            )
            db.session.add(cocktail)
            logger.info(f"Added cocktail: {cocktail.name}")

            # Add Ingredients
            for ingredient_str in cocktail_data['ingredients']:
                parts = ingredient_str.split(' ', 1)
                amount = parts[0] if len(parts) > 1 else ''
                name = parts[1] if len(parts) > 1 else parts[0]

                # Check if ingredient already exists
                ingredient = Ingredient.query.filter_by(name=name).first()
                if not ingredient:
                    ingredient = Ingredient(name=name)
                    db.session.add(ingredient)
                    logger.info(f"Added new ingredient: {name}")

                # Create association between cocktail and ingredient
                cocktail_ingredient = CocktailIngredient(
                    cocktail=cocktail,
                    ingredient=ingredient,
                    amount=amount
                )
                db.session.add(cocktail_ingredient)
                logger.info(f"Linked {ingredient.name} to {cocktail.name}")

        db.session.commit()
        logger.info("Seeding process completed successfully!")

    except Exception as e:
        logger.error(f"Error during seeding: {str(e)}")
        db.session.rollback()

if __name__ == '__main__':
    with app.app_context():
        seed_data()
