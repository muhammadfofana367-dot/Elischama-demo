from django.urls import path
from .views import CreateServiceView


app_name = 'services'

urlpatterns=[
    path('create/', CreateServiceView.as_view(), name='create_service'),
]

