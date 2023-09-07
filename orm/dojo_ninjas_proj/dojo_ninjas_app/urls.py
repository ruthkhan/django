from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('dojos/create', views.new_dojo), 
    path('ninjas/create', views.new_ninja),
    path('dojos/delete/<int:dojo_id>', views.delete),
]
