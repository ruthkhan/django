from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    path('plus2', views.plus2),
    path('plus_x', views.plus_x),
]
