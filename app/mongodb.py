from app import app

COLLECTION_NAME = 'recipes'

def mongo_db() :
    return app.config['pymongo_db'].db

def remove_Recipes():
    mongo_db()[COLLECTION_NAME].remove()
    return

def insert_recipe(recreate_db = False):
    """
        Inserts population data into database
        clears existing data if recreate_db = True
    """
    if (recreate_db):
        remove_Recipes()
    # Convert it to Json
    try:
        records ={
        'title': 'spinach corn sandwich',
        'sourceUrl': 'https://hebbarskitchen.com/spinach-corn-sandwich-recipe/',
        'cookingMinutes': 10,
        'image': 'https://spoonacular.com/recipeImages/1047695-556x370.jpg',
        'instructions': 'Instructionsfirstly, in a large tawa heat 1 tsp butter and saute 2 tbsp onion.',
        'ingredients': ['1 tsp butter', '2 tbsp onion finely chopped', '1 cup palak / spinach finely chopped']},
        {'title': 'spinach corn sandwich',
        'sourceUrl': 'https://hebbarskitchen.com/spinach-corn-sandwich-recipe/',
        'cookingMinutes': 10,
        'image': 'https://hebbarskitchen.com/wp-content/uploads/mainPhotos/onion-tomato-chutney-recipe-tomato-onion-chutney-recipe-1.jpeg',
        'instructions': 'Instructionsfirstly, in a large tawa heat 1 tsp butter and saute 2 tbsp onion.',
        'ingredients': ['1 tsp butter', '2 tbsp onion finely chopped', '1 cup palak / spinach finely chopped']
        }
        # Insert only if place does not exist
        # if (mongo_db()['population']
        #             .find({"place_id": location.raw["place_id"]})
        #             .count() == 0):
        #     print(records)
        #     mongo_db()['population'].insert(records)
        # else:
        #     print("updating")
        # mongo_db()['population'].update({"place_id": records["place_id"]},
        #     records, upsert=True)
        mongo_db()[COLLECTION_NAME].insert(records)
        print("Inserted record please check ...")
    except Exception as e:
        print(e)
