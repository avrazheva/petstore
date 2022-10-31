install:
	poetry install --no-dev

client:
	swagger_codegen generate ./petstore.yaml ./petstore

test:
	poetry run pytest tests/ -n auto --alluredir=allure-report/
