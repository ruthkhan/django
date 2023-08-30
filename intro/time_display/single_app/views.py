from django.shortcuts import render, HttpResponse
from time import localtime, strftime


# Create your views here.
def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime())
    }
    return render(request,"index.html", context)