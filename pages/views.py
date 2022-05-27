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
    