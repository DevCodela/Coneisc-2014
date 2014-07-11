# Web Platform #

Este repositorio es un ejercicio para poner en práctica Django Rest Framework y Backbone.js.

### Requirements ###

* Virtualenv or virtualenvwrapper
* Django 1.6.5
* Django Rest Framework
* Etc

### Create a virtualenv ###

* Usando virtualenv

    $ virtualenv env
    $ source env/bin/activate

* Usando virtualenvwrapper

    $ mkvirtualenv webplatform
    $ workon webplatform

    $ rmvirtualenv webplatform

### PostgreSQL

    $ su postgres
    $ psql
    postgres=# CREATE DATABASE webplatformdb;
    postgres=# CREATE USER webplatformuser WITH ENCRYPTED PASSWORD 'userpass';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE webplatformdb to webplatformuser;

### Installing from requirements files (local or staging)

    $ pip install -r requirements/local.txt

    $ pip install -r requirements.txt

### Collectstatics (local)

    $ python manage.py collectstatic --settings=webplatform.settings.staging

### South (local)

    $ python manage.py schemamigration tienda --initial --settings=webplatform.settings.local
    $ python manage.py migrate tienda --settings=webplatform.settings.local

### How to run the project (local)

    $ python manage.py runserver --settings=webplatform.settings.local

### Heroku Deploy

    $ pwd --> /home/[your_user]/projects/webplatform_project/webplatform/
    
    $ heroku login
    
    $ git init
    $ git add .
    $ git commit -m "First Commit"

    $ heroku create [app_name]
    $ git push heroku master

    $ heroku run python manage.py syncdb --settings=webplatform.settings.staging

    $ heroku open

# NOTE: Permmisions error

    $ heroku keys:add