.PHONY: run test test-verbose test-coverage test-coverage-html

run:
	python app/Main.py

test:
	pytest tests/

test-verbose:
	pytest tests/ -v

test-coverage:
	pytest --cov-report=term-missing --cov=app tests/

test-coverage-html:
	pytest tests/ --cov=app --cov-report=html


