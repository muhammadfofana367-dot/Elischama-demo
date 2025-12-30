from django.urls import path
from .views import ServiceView, TrainingView, AboutView, ContactView, HomeView



app_name = 'core'

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('service/', ServiceView.as_view(), name='service'),
    path('training/', TrainingView.as_view(), name='training'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]