from model.recipe import Recipe


# fake data, until we use a real database and SQL
_recipes = [
    Recipe(recipe_id=0,
           owner_id=0,
           name="Grilled Cheese", 
           ingredients="""1. 2 slices of bread
           2. 1 slice of cheese (any)
           3. 1t butter""",
           notes="Good for a quick snack",
           steps="""1. Spread butter evenly on one side of both pieces of bread
           2. Place one slice of bread face down in a warm skillet
           3. Place slice of cheese on top of bread
           4. Place the remianing slice of bread on top, with butter facing up
           5. Grill each side for 2-5 minutes until browned""",
           serves=1,
           prep_time=5,
           cook_time=10
    ),
    Recipe(recipe_id=1,
        owner_id=1,
        name="Pizza Dough", 
        ingredients="""200g water
        153g 00 flour (can be subbed for all purpose flour)
        153g all purpose flour
        8g fine sea salt
        2g active dry yeast
        4g EVOO""",
        notes="The dough is best if allowed to rise in the fridge for between 1 and 3 days.",
        steps="""1. Combine flours and salt in a large bowl. Add water, yeast and EVOO and lightly mix for 3 minutes. Let rest for 15 minutes.
        2. Knead for an additional 3 minutes. Divide in half and place on heavily floured surface.
        3. Let rise for 3-4 hours or overnight before cooking. If rising overnight, let the dough sit out for 30-45 minutes.
        4. Bake at highest possible temperature for about 5 minutes. (500-550°)""",
        serves=4,
        prep_time=180,
        cook_time=10
        ),
    ]

def get_all() -> list[Recipe]:
    """Return all recipes"""
    return _recipes

def get_one(name: str) -> Recipe | None:
    """Return one recipe"""
    for _recipe in _recipes:
        if _recipe.name == name:
            return _recipe
    return None

def create(recipe: Recipe) -> Recipe:
    """Add a recipe"""
    return recipe

def modify(recipe: Recipe) -> Recipe:
    """Partially modify a recipe"""
    return recipe

def delete(name: str):
    """Delete a recipe; return None if it existed"""
    return None