from django.shortcuts import render, redirect
import random

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
    }
    return render(request, "index.html", context)

def check(request): 
    request.session['tries'] +=1
    guessed = int(request.POST['number'])
    answer = str(request.session['number']) + " was the number!"
    if guessed < request.session['number'] and request.session['tries'] <= 5: 
        request.session['comment'] = "Too low!"
        request.session['status'] = "wrong"
        return redirect('/')
    elif guessed > request.session['number'] and request.session['tries'] <= 5: 
        request.session['comment'] = "Too high!"
        request.session['status'] = "wrong"
        return redirect('/')
    elif request.session['tries'] > 5: 
        request.session['comment'] = "You Lose! " + answer
        request.session['status'] = "wrong"
        return redirect('/')
    else: 
        request.session['status'] = "right"
        request.session['comment'] = "You Win! " + answer
        return redirect('/')

# def lose(): 
#     return render_template("lose.html", comment=session['comment'], tries=session['tries'])

# @app.route('/correct')
# def correct(): 
#     return render_template("correct.html", comment=session['comment'], tries=session['tries'])

def reset(request): 
    request.session.clear()
    return redirect('/')

# @app.route('/leader', methods=["POST"])
# def leader():
#     if len(leaderboard) == 0: 
#         leaderboard.append({'name':request.form['leader'], 'tries':session['tries']})
#     else: 
#         for i in range(len(leaderboard)): 
#             if session['tries'] <= leaderboard[i]['tries']: 
#                 leaderboard.insert(i, {'name':request.form['leader'], 'tries':session['tries']})
#                 break
#             elif i == (len(leaderboard)-1): 
#                 leaderboard.append({'name':request.form['leader'], 'tries':session['tries']})
#             else: 
#                 continue
#     return render_template("leader.html", leaderboard=leaderboard)

# @app.route('/viewboard', methods=["POST"])
# def viewboard(): 
#     return render_template("leader.html", leaderboard=leaderboard)
