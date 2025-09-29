dev:
	RECIPE_SQLITE_DB=recipes.db python src/main.py
test:
	RECIPE_SQLITE_DB=":memory:" pytest -v src/test;