from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Autenticação'}
        ), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),
    path('mudar_senha/', views.change_password, name='mudar_senha')
]
