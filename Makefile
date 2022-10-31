install:
	poetry install --no-dev

lint:
	poetry run isort .
	poetry run flake8 .

client:
	swagger_codegen generate ./petstore.yaml ./petstore

test:
	poetry run pytest tests/ -n auto --alluredir=allure-report/

report:
	poetry run allure serve allure-report
