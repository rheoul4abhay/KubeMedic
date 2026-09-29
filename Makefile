.PHONY: install test lint format run

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

run:
	uvicorn kubemedic.api.main:app --reload
