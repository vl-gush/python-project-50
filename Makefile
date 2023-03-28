build: check
	poetry build

check: selfcheck test lint

install:
	poetry install

lint:
	poetry run flake8 gendiff

package-install:
	python3 -m pip install --force-reinstall --user .

publish:
	poetry publish --dry-run

selfcheck:
	poetry check

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

.PHONY: build check install lint package-install publish selfcheck test test-coverage