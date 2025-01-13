install-requirements:
	pip install --upgrade pip
	pip install -r requirements.txt -U

server:
	python manage.py migrate && python manage.py runserver

run-celery-server:
	celery -A maltina worker --loglevel DEBUG  --concurrency=1

makemessages:
	python manage.py makemessages -l fa --ignore venv

compilemessages:
	python manage.py compilemessages -l fa

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	python manage.py test

flake8:
	. venv/bin/activate && flake8