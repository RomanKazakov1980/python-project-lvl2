install:
	poetry install

build:
	poetry build

publish:
	poetry poblish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

run:
	poetry run gendiff

test:
	poetry run pytest -vv

check: test lint

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml