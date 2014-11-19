VENV_NAME ?= venv
PIP ?= pip

ACTIVATE_VENV = . $(VENV_NAME)/bin/activate

pip: venv
	$(ACTIVATE_VENV) && $(PIP) install -r pip_requirements.txt

venv:
	virtualenv -p python3 $(VENV_NAME)

runserver:
	$(ACTIVATE_VENV) && basetestsite/manage.py runserver

