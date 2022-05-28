import operator
from xmlrpc.client import DateTime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils import timezone
import datetime
from django.contrib import messages
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.mail import send_mail
User = get_user_model()

from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,'home.html',{})
def interests_view(request):
    if request.method == 'POST':
        choice_list = request.POST.getlist('selection')
        for choice in choice_list:
            user = request.user
            id = user.id
            if choice == "computer_science":
                User.objects.filter(id=id).update(computer_science=True)
            if choice == "cyber_security":
                User.objects.filter(id=id).update(cyber_security=True)
            if choice == "ai":
                User.objects.filter(id=id).update(ai=True) 
            if choice == "design":
                User.objects.filter(id=id).update(design=True) 
            if choice == "it_systems":
                User.objects.filter(id=id).update(it_systems=True) 
            if choice == "iot":
                User.objects.filter(id=id).update(iot=True) 
            if choice == "software":
                User.objects.filter(id=id).update(software=True) 
            if choice == "data_science":
                User.objects.filter(id=id).update(data_science=True) 
            if choice == "networks":
                User.objects.filter(id=id).update(networks=True) 
            if choice == "books":
                User.objects.filter(id=id).update(books=True) 
            if choice == "movies":
                User.objects.filter(id=id).update(movies=True) 
            if choice == "music":
                User.objects.filter(id=id).update(music=True) 
            if choice == "signing":
                User.objects.filter(id=id).update(signing=True) 
            if choice == "mangas":
                User.objects.filter(id=id).update(mangas=True) 
            if choice == "animes":
                User.objects.filter(id=id).update(animes=True) 
            if choice == "series":
                User.objects.filter(id=id).update(series=True) 
            if choice == "drawing":
                User.objects.filter(id=id).update(drawing=True) 
            if choice == "hiking":
                User.objects.filter(id=id).update(hiking=True) 
            if choice == "football":
                User.objects.filter(id=id).update(football=True) 
            if choice == "tennis":
                User.objects.filter(id=id).update(tennis=True)   
            if choice == "cooking":
                User.objects.filter(id=id).update(cooking=True) 
            if choice == "basketball":
                User.objects.filter(id=id).update(basketball=True)
            if choice == "handball":
                User.objects.filter(id=id).update(handball=True)
            if choice == "volleyball":
                User.objects.filter(id=id).update(volleyball=True)
            if choice == "fitness":
                User.objects.filter(id=id).update(fitness=True)
            if choice == "jogging":
                User.objects.filter(id=id).update(jogging=True)
            if choice == "cyclism":
                User.objects.filter(id=id).update(cyclism=True)
        return redirect("home")
    return render(request, 'interests.html', {})

def matching_view(request):
    users = User.objects.all()
    print(users)
    search_wilaya = request.POST.get('user_wilaya', None)
    print(search_wilaya)
    search_level = request.POST.get('level', None)
    li = []
    if search_wilaya != "0" and search_wilaya != None:
        users = users.filter(wilaya = search_wilaya)
        li.append(search_wilaya)
    print(users)
    if search_level != "0" and search_level != None:
        users = users.filter(year = search_level)
        li.append(search_level)
    current_user = request.user
    somme = 0
    l = []
    for user in users :
        if user.id != current_user.id:
            if user.computer_science == True and current_user.computer_science == True:
                somme += 1
            if user.cyber_security == True and current_user.cyber_security == True:
                somme += 1
            if user.ai == True and current_user.ai == True:
                somme += 1
            if user.design == True and current_user.design == True:
                somme += 1
            if user.it_systems == True and current_user.it_systems == True:
                somme += 1
            if user.iot == True and current_user.iot == True:
                somme += 1
            if user.software == True and current_user.software == True:
                somme += 1
            if user.data_science == True and current_user.data_science == True:
                somme += 1
            if user.networks == True and current_user.networks == True:
                somme += 1
            if user.books == True and current_user.books == True:
                somme += 1
            if user.movies == True and current_user.movies == True:
                somme += 1
            if user.music == True and current_user.music == True:
                somme += 1
            if user.signing == True and current_user.signing == True:
                somme += 1
            if user.mangas == True and current_user.mangas == True:
                somme += 1
            if user.animes == True and current_user.animes == True:
                somme += 1
            if user.series == True and current_user.series == True:
                somme += 1
            if user.drawing == True and current_user.drawing == True:
                somme += 1
            if user.hiking == True and current_user.hiking == True:
                somme += 1
            if user.football == True and current_user.football == True:
                somme += 1
            if user.tennis == True and current_user.tennis == True:
                somme += 1
            if user.cooking == True and current_user.cooking == True:
                somme += 1
            if user.basketball == True and current_user.basketball == True:
                somme += 1
            if user.handball == True and current_user.handball == True:
                somme += 1
            if user.volleyball == True and current_user.volleyball == True:
                somme += 1
            if user.fitness == True and current_user.fitness == True:
                somme += 1
            if user.jogging == True and current_user.jogging == True:
                somme += 1
            if user.cyclism == True and current_user.cyclism == True:
                somme += 1
            l .append([somme,user.id])
    sorted_list = sorted(l, key=lambda x: x[1])
    users = users.filter(username = '')
    for element in sorted_list :
        users = users.union(User.objects.filter(id = element[1]))
    context = {
        'users' : users,
        'list' : li
    }
    return render(request, 'matching.html', context)


def quizz(request):
    if request.method == 'POST':
        choice_list = request.POST.getlist('selection')
        somme = 0
        for choice in choice_list :
            if (choice == 1) or (choice == 5) or (choice == 9) or (choice == 13) or (choice == 19) or (choice == 22) or (choice == 28) :
                somme += 1
        user = request.user
        id = user.id
        users = User.objects.filter(id = id)
        users.update(note_quizz = somme)
        return redirect("dashboard")
    return render(request, 'quizz.html')

def classement(request):
    users = User.objects.all()
    l = []
    for user in users :
        l.append([user.note_quizz,user.id])
    sorted_list = sorted(l, key=lambda x: x[1])
    users = users.filter(username = '')
    for element in sorted_list :
        users = users.union(User.objects.filter(id = element[1]))
    context = {
        'users' : users,
        'range': range(1,11)
    }
    return render(request, 'classement.html',context)

def dashboard(request):
    return render(request,'dashboard.html')

def galerie(request):
    return render(request,'galerie.html')

def profile(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request, 'profile.html', context)

def mentors(request):
    users = User.objects.exclude(year = "1cp")
    context = {
        "users" : users
    }
    return render(request,'mentors.html',context)

def culture(request):
    return render(request,'kabyle_culture.html')

def personalities(request):
    return render(request,'kabyle_personalities.html')

def home2(request):
    return render(request,'home2.html')

def contactus(request):
    return render(request,'contactus.html')

def messagerie(request):
    return render(request,'messagerie.html')

def homepage(request):
    return render(request,'homepage.html')

def discover(request):
    return render(request,'discover.html')