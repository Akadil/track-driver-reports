from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicles_page, name='vehicles_page'),
    path('<int:id>/', views.vehicle_detail_page, name='vehicle_detail_page'),
    # path('add/', views.add_vehicle, name='add_vehicle'),
]