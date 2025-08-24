install:
	pip install -r requirements.txt

lint:
	ruff check . && black --check . && mypy src

test:
	pytest -q --cov=src --cov-fail-under=85

sec:
	bandit -r src && pip-audit
