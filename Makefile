run:
	python3 -m venv .env && \
	source .env/bin/activate && \
	pip install -r requirements.txt && \
	pip install -e . && \
	python solver_eval/test_all.py

test:
	python3 -m venv .env && \
	source .env/bin/activate && \
	pip install -r requirements.txt && \
	pytest


