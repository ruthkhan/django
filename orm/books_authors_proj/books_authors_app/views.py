from django.shortcuts import render, redirect
from .models import Book, Author

# Book Views
def index(request): 
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def create_book(request): 
    Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')

def get_book(request, book_id): 
    this_book = Book.objects.get(id=book_id)
    context = {
        "id": book_id,
        "title": this_book.title, 
        "description": this_book.desc, 
        "author_data": this_book.authors.all(),
        "all_authors": Author.objects.exclude(books=this_book),
    }
    return render(request, "book.html", context)

def add_book_author(request): 
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_book.authors.add(Author.objects.get(id=request.POST['author_id']))
    origin = request.POST['origin']
    return redirect(f'/{origin}')

# Author Views
def authors(request): 
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def create_author(request): 
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')

def get_author(request, author_id): 
    this_author = Author.objects.get(id=author_id)
    context = {
        "id": author_id,
        "first_name": this_author.first_name, 
        "last_name": this_author.last_name,
        "notes": this_author.notes, 
        "book_data": this_author.books.all(),
        "all_books": Book.objects.exclude(authors=this_author),
    }
    return render(request, "author.html", context)