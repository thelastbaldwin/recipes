from model.recipe import Recipe
from service import recipe as code

sample = Recipe(recipe_id = "0",
           owner_id = "0",
           name="Grilled Cheese", 
           notes="Good for a quick snack",
           ingredients="""1. 2 slices of bread
           2. 1 slice of cheese (any)
           3. 1t butter""",
           steps="""1. Spread butter evenly on one side of both pieces of bread
           2. Place one slice of bread face down in a warm skillet
           3. Place slice of cheese on top of bread
           4. Place the remianing slice of bread on top, with butter facing up
           5. Grill each side for 2-5 minutes until browned""",
           serves=1,
           prep_time=5,
           cook_time=10,
           )

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one("Grilled Cheese")
    assert resp == sample

def test_get_missing():
    resp = code.get_one("boxturtle")
    assert resp is None