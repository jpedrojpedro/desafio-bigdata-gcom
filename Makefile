.PHONY: setup test run help

setup:
	@echo 'Instalando dependências da API'
	@echo 'Flask + SQLite3'
	cd app && docker-compose build api
	@echo 'Setup finalizado'

test:
	@echo 'Executando testes'
	@echo 'Implementar...'

run:
	@echo 'Iniciando aplicação'
	@echo 'Disponibilizando API'
	cd app && docker-compose up api

GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

TARGET_MAX_CHAR_NUM=30
## Show help
help:
	@echo ''
	@echo 'Uso:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(helpLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")); \
			helpMessage = substr(helpLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ helpLine = $$0 }' $(MAKEFILE_LIST)
