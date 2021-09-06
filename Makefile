all:
	python manage.py runserver

install:
	python -m pip install -r requirements.txt

migrate:
	python manage.py migrate

app:
	python manage.py startapp $(APP_NAME)
