VENV_NAME ?= venv
PIP ?= pip

ACTIVATE_VENV = . $(VENV_NAME)/bin/activate
MANAGE = basetestsite/manage.py

pip: venv
	$(ACTIVATE_VENV) && \
	$(PIP) install -r pip_requirements.txt && \
	$(PIP) install -e .

venv:
	virtualenv -p python3 $(VENV_NAME)

runserver:
	$(ACTIVATE_VENV) && $(MANAGE) runserver

test:
	$(ACTIVATE_VENV) && $(MANAGE) test dcbase
