from django.contrib.auth import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.teste)
]