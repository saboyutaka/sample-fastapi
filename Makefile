.DEFAULT_GOAL := help

build: ## build develoment environment without workspace
	docker-compose run --rm python pip install -r requirements.txt --user

serve: ## Run Server without workspace
	docker-compose up python

pip-install: ## Run pip install with workspace
	pip install -r requirements.txt --user

run: ## Run FastAPI with workspace
	uvicorn main:app --reload --host 0.0.0.0 --port 7000

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
