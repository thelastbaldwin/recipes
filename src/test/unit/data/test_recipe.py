from model.user import User
from model.recipe import Recipe
from data import recipe, user
from errors import Missing
import pytest

@pytest.fixture
def seed():
    sample_user = User(
        email="test@test.com",
        username="test_user",
        password_hash="123456"
    )

    user_response = user.create(sample_user)

    sample_recipe = Recipe(
            owner_id = user_response.user_id,
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
    
    recipe_response = recipe.create(sample_recipe)
    yield user_response, recipe_response

    recipe.delete(recipe_response.recipe_id)
    user.delete(user_response.user_id)

def test_get_one_exists(seed):
    _, recipe_seed = seed
    resp = recipe.get_one(recipe_seed.recipe_id)
    assert resp == recipe_seed

def test_get_one_missing():
    with pytest.raises(Missing):
        recipe.get_one(1)

def test_get_all(seed):
    resp = recipe.get_all()
    assert len(resp) == 1

def test_get_all_empty():
    resp = recipe.get_all()
    assert len(resp) == 0

def test_modify(seed):
    _, recipe_seed = seed
    clone = recipe_seed.model_copy(deep=True)
    clone.ingredients = "throw everything in the trash"
    clone.notes = "eat if you dare"
    clone.steps = "0. don't even try"
    clone.serves = 4
    clone.prep_time = 15
    clone.cook_time = 11
    resp = recipe.modify(recipe_seed.recipe_id, clone)
    assert resp == clone

def test_modify_missing(seed):
    _, recipe_seed = seed
    clone = recipe_seed.model_copy(deep=True)
    clone.ingredients = "throw everything in the trash"
    clone.notes = "eat if you dare"
    clone.steps = "0. don't even try"
    clone.serves = 4
    clone.prep_time = 15
    clone.cook_time = 11

    with pytest.raises(Missing):
        bad_id = 6
        recipe.modify(bad_id, clone)

def test_delete_missing():
    with pytest.raises(Missing):
        recipe.delete(6)