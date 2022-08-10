from unicodedata import name
from django.contrib.auth import admin
from django.urls import include, path
from . import views

app_name = 'tcc'

urlpatterns = [
    path('', views.home, name='home'),
    path('tccs/<int:id>', views.tcc, name='tcc'),
    path('<model>/criar', views.criar, name='criar'),
    # path('autor_criar', views.autor_criar, name='criar_autor'),
]