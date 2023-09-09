from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('books/<int:book_id>', views.get_book),
    path('add_book_author', views.add_book_author),
    path('authors', views.authors),
    path('create_author', views.create_author), 
    path('authors/<int:author_id>', views.get_author),
]
