install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user .

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

.PHONY: install build lint publish package-install test