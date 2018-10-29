from django.http import HttpResponse
import os
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def files(request):
    a = """mkdir django
cd django
python -m venv django_env
activate virtual env
==============
linux- django_env/bin/active
windows- django_env/Scripts/activate.bat

install Django
=========
liux
pip install django
or 
pip install django==1.9

=====================
upgrade pip 
python -m pip install --upgrade pip

===========
create a new project

django-admin startproject raja
cd raja
python manage.py runserver

add pge to django

views.py

APP
Models
Migrations
-models , views and templates are the core components of the django
Creating app
python manage.py showmigrations
python mange.py migrte 	
python manage.py startapp gameplay
add model classes
"""
    html1 = "<html><body> <p>Sincerely,<br />{{ %s }}</p></body></html>" % a
    return HttpResponse(html1)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_behind(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() - datetime.timedelta(hours=offset)
    html = "<html><body>%s hour(s) ago, it was %s.</body></html>" % (offset, dt)
    return HttpResponse(html)




