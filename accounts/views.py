from django.shortcuts import render
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
from .forms import ImageUpdate

from django.shortcuts import render

# Create your views here.
def image_view(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request,'photo.html',context)

def updateimage(request, id):  
    data = CustomUser.objects.get(id=id)
    form = ImageUpdate(request.POST,request.FILES,instance = data)
    if form.is_valid():
        form.image = request.FILES['image']
        form.save()
    return redirect('profile')
