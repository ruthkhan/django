from django.shortcuts import render, redirect
import random
from datetime import datetime 

# Create your views here.
def index(request): 
    if 'state' in request.session: # call alert box and display reset button if person has won/lost
        state = request.session['state']
    else: # set default values for a new game
        state = ""
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['moves'] = 0
    context = {
        "gold": request.session['gold'], 
        "activities": request.session['activities'], 
        "state": state,
    }
    return render(request, "index.html", context)

def process_money(request, location): 
    if location == "farm": 
        gold_min = -10
        gold_max = 20
    elif location == "cave": 
        gold_min = -5
        gold_max = 10
    elif location == "house": 
        gold_min = 2
        gold_max = 5
    elif location == "casino": 
        gold_min = -50
        gold_max = 50
    gold = random.randint(gold_min,gold_max) 
    timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    color = "green" # color of text in activity log
    request.session['state'] = "playing" # win, lose, or playing

    if gold >= 0: # generate activity log message; different color and message if money lost
        message = f"<p class='my-0' style='color: {color};'>Earned {gold} gold from the {location}! ({timestamp})</p>"
    else: 
        color = "red"
        message = f"<p class='my-0' style='color: {color}'>Entered a {location} and lost {-gold} gold... Ouch.. ({timestamp})</p>"
    
    request.session['activities'].insert(0, message) # update activity log, gold, and count of moves
    request.session['gold'] +=gold
    request.session['moves'] +=1
    if request.session['gold'] >= 50: # determine if user has won; user wins if gold > 50 
        request.session['state'] = "win()"
    elif request.session['moves'] >= 15: # determine if user has lost; user loses if gold < 50 and moves > 15
        request.session['state'] = "lose()"
    
    return redirect("/")

def reset(request): 
    request.session.clear()
    return redirect("/")