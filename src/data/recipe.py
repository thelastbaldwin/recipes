from .init import (curs, conn, IntegrityError)
from model.recipe import Recipe
from errors import Missing

def row_to_model(row: tuple) -> Recipe:
    recipe_id, owner_id, name, notes, ingredients, steps, serves, prep_time, cook_time = row
    return Recipe(recipe_id=recipe_id, owner_id=owner_id, name=name, notes=notes, ingredients=ingredients, steps=steps, serves=serves, prep_time=prep_time, cook_time=cook_time)

def model_to_dict(recipe: Recipe) -> dict:
    return recipe.model_dump()

def get_one(recipe_id: int) -> Recipe:
    qry = "SELECT * FROM recipe WHERE recipe_id=:recipe_id"
    params = {"recipe_id": recipe_id}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Recipe {recipe_id} not found")

def get_all() -> list[Recipe]:
    qry = "SELECT * FROM recipe"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(recipe: Recipe) -> Recipe:
    qry = """INSERT INTO recipe (owner_id, name, notes, ingredients, steps, serves, prep_time, cook_time) VALUES
          (:owner_id, :name, :notes, :ingredients, :steps, :serves, :prep_time, :cook_time)"""
    params = model_to_dict(recipe)
    curs.execute(qry, params)
    return get_one(curs.lastrowid)

def modify(recipe_id: int, recipe: Recipe) -> Recipe:
    qry = """UPDATE recipe
             SET name=:name,
             notes=:notes,
             ingredients=:ingredients,
             steps=:steps,
             serves=:serves,
             prep_time=:prep_time,
             cook_time=:cook_time
             WHERE recipe_id=:recipe_id"""
    params = model_to_dict(recipe)
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(recipe_id)
    else:
        raise Missing(msg=f"Recipe {recipe_id} not found")

def delete(recipe_id: int):
    if not recipe_id: return False
    qry = "DELETE FROM recipe WHERE recipe_id = :recipe_id"
    params = {"recipe_id": recipe_id}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Recipe {recipe_id} not found")