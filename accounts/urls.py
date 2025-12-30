from django.contrib.auth.views import LoginView, LogoutView
from .views import PerfilView, RegistroView
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='paginas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/',  PerfilView.as_view(), name='perfil'),
    path('registro/', RegistroView.as_view(), name='registro'),
]
