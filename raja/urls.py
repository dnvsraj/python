"""raja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import current_datetime
from .views import files
from .views import hours_ahead,hours_behind
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'now/date', current_datetime),
    path(r'files', files),
    path(r'^now/plus(\d{1,2})hours/$', hours_ahead),
    path(r'^now/minus(\d{1,2})hours/$', hours_behind),
    ]
