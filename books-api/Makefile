.PHONY: venv
venv:
	test -f venv/bin/python || python3 -m venv venv
	venv/bin/pip install -q -U pip


.PHONY: deps
deps: venv
	venv/bin/python3 -m pip install -q -r requirements.txt


.PHONY: deps-dev
deps-dev: venv
	venv/bin/python3 -m pip install -q -r requirements-dev.txt

.PHONY: build
build: deps
	venv/bin/pip install -r requirements.txt --target python
	cp -r templates python
	cp lambda_function.py python
	(cd python; zip -r ../app ./)

.PHONY: run
run: deps-dev
	venv/bin/python3 -m flask --app lambda_function:app --debug run


.PHONY: format
format: deps-dev
	venv/bin/python3 -m black .
	venv/bin/python3 -m isort .


.PHONY: lint
lint: deps-dev
	venv/bin/python3 -m black . --check
	venv/bin/python3 -m flake8 .
	venv/bin/python3 -m isort . --check
	venv/bin/python3 -m mypy .


.PHONY: test
test: deps-dev
	venv/bin/python3 -m pytest -v
