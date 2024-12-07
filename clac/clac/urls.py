from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.calculate_power, name='calculate_power'),
]