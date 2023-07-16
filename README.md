# django-demo

python --version

# install django (backend framework)
cd django
pipenv install django
pipenv shell

# start project
pipenv install djangorestframework

django-admin startproject myproject .
python manage.py startapp playground

# migration
python manage.py makemigrations
python manage.py migrate

# run server
python manage.py runserver 0.0.0.0:8000

# add codespace conf file
git add .devcontainer/devcontainer.json
