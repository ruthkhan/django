from django.shortcuts import render, redirect

# Create your views here.
def index(request): 
    if 'visits' not in request.session: 
        request.session['visits'] = 1
        request.session['count'] = 1
    else: 
        request.session['visits'] +=1 
        request.session['count'] +=1
    return render(request, 'index.html')

def destroy_session(request): 
    request.session.clear()
    return redirect ("/")

def plus2(request): 
    request.session['count'] +=1
    return redirect("/")

def plus_x(request): 
    request.session['count'] += (int(request.POST['increment'])-1)
    return redirect("/")