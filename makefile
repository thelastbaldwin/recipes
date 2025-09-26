dev:
	CRYPTID_SQLITE_DB=cryptid.db; python src/main.py
test:
	pytest -v src/test