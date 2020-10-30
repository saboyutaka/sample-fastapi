.DEFAULT_GOAL := help

build: ## build develoment environment
	docker-compose run --rm python pip install -r requirements.txt --user

serve: ## Run Server
	docker-compose up python

pip-install: ## Run route:list
	docker-compose run --rm python pip install -r requirements.txt --user

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
