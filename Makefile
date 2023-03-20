install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user .

lint:
	poetry run flake8 brain_games

.PHONY: install build publish package-install lint