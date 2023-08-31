from django.shortcuts import render, redirect
import random

leaderboard = []

# Create your views here.
def index(request):
    if 'tries' not in request.session: 
        request.session['number'] = random.randint(1, 100)
        request.session['comment'] = ""
        request.session['tries'] = 0
        request.session['status'] = "start"
    context = {
        "comment": request.session['comment'],
        "container": request.session['status'],
        "number": request.session['number'],
        "tries": request.session['tries'],
    }
    # print (request.session['number']) - for checking
    return render(request, "index.html", context)

def check(request): 
    guessed = int(request.POST['number'])
    answer = str(request.session['number']) + " was the number!"
    if guessed < request.session['number'] and request.session['tries'] < 5: 
        request.session['comment'] = "Too low!"
        request.session['status'] = "wrong"
    elif guessed > request.session['number'] and request.session['tries'] < 5: 
        request.session['comment'] = "Too high!"
        request.session['status'] = "wrong"
    elif guessed != request.session['number'] and request.session['tries'] >= 5: 
        request.session['comment'] = f"You Lose! {answer}"
        request.session['status'] = "wrong"
    else: 
        request.session['status'] = "right"
        attempts = int(request.session['tries']) + 1
        request.session['comment'] = f"You Win! {answer} You took {attempts} attempts."
    request.session['tries'] +=1
    return redirect('/')

def reset(request): 
    request.session.clear()
    return redirect('/')

def leader(request):
    if len(leaderboard) == 0: #if nobody else on leaderboard, add to board anywhere
        leaderboard.append({'name':request.POST['leader'], 'tries':request.session['tries']})
    else: 
        for i in range(len(leaderboard)): #iterate through existing leaders to see where to insert this score
            if request.session['tries'] <= leaderboard[i]['tries']: 
                leaderboard.insert(i, {'name':request.POST['leader'], 'tries':request.session['tries']})
                break
            elif i == (len(leaderboard)-1): 
                leaderboard.append({'name':request.POST['leader'], 'tries':request.session['tries']})
            else: 
                continue
    return redirect("/viewboard")

def viewboard(request): 
    context = {
        "leaderboard": leaderboard,
    }
    return render(request, "leader.html", context)
