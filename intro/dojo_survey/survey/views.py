from django.shortcuts import render

def index(request): 
# Create your views here.
    return render(request, "index.html")

def result(request): 
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comments = request.POST['comments']
    context = {
    	"name" : name,
    	"location" : location, 
        "language" : language, 
        "comments" : comments,
    }
    return render(request, "show.html", context)