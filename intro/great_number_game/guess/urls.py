from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('check', views.check), 
    path('reset', views.reset), 
    path('leader', views.leader),
    path('viewboard', views.viewboard),
]
