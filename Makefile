run:
	poetry run python src/cli.py
install:
	poetry install
qa: format lint typecheck
test:
	poetry run pytest -vv
lint:
	poetry run flakeheaven lint
format:
	poetry run black .
typecheck:
	poetry run mypy .
