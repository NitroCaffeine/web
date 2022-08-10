from django.urls import path

from tcc import views

app_name = 'tcc'

urlpatterns = [
    path('', views.home, name='home'),
    path('tccs/<int:id>', views.tcc, name='tcc'),
    path('criar/<model>', views.criar, name='criar'),
    path('listar/<model>', views.listar, name='listar'),
    # path('atualizar/<model>/<int:id>', views.atualizar, name='criar'),
    # path('deletar/<model>/<int:id>', views.deletar, name='criar'),
]
>>>>>>> 60ffc6789874fbc16bf0d027fa3a8852ffa59f87
