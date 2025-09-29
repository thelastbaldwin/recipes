dev:
	RECIPE_SQLITE_DB=recipes.db python src/main.py

test: export RECIPE_SQLITE_DB=:memory:
test:
	pytest -v src/test;