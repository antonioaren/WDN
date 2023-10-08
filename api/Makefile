.PHONY: format

format: isort black

black:
	poetry run black --extend-exclude='/migrations/' .

isort:
	poetry run isort .