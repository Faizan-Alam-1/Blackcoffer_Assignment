
from django.urls import path
from . import views

urlpatterns = [
    path('energy-data/', views.energy_data_list, name='energy-data-list'),
    
]
