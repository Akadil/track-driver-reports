from django.urls import path
from . import views

urlpatterns = [
    path('', views.drivers_page, name='drivers_page'),
]