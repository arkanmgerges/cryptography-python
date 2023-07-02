test_with_coverage:
	poetry run pytest -vv --cov=src --cov-report=term-missing --cov-fail-under=100 tests/

test:
	poetry run pytest -vv

.PHONY: test test_with_coverage