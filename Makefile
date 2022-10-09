SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c # bash strict mode https://tech.davis-hansson.com/p/make/
.ONESHELL: # one single shell session for a make recipe
.DELETE_ON_ERROR: # if a Make rule fails, its target file is deleted
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ci: lint test ## Run all checks (test, lint, typecheck)

test:  ## Run tests
	poetry run pytest .

lint:  ## Run linting
	poetry run black --check .
	poetry run isort -c .
	# poetry run sqlfluff lint sql/

fix:  ## Run autoformatters
	poetry run black .
	poetry run isort .
	# poetry run sqlfluff fix sql/

clean:
	rm -rf data/sink
	mkdir data/sink
	find . -name '__pycache__' -type d | xargs rm -fr

.PHONY: ci test lint fix clean
