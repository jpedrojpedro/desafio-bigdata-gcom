.PHONY: setup test run

setup:
	@echo 'Instalando dependências da API'
	@echo 'Flask + SQLite3'
	cd app && docker-compose build api
	cd app && docker-compose build test
	@echo 'Setup finalizado'

test:
	@echo 'Executando testes'
	cd app && docker-compose up test

run:
	@echo 'Iniciando aplicação'
	@echo 'Disponibilizando API'
	cd app && docker-compose up api
