from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

def audio_store(request):
    audio1 = Audio_store.objects.get(id = 2)
    audio2 = Audio_store.objects.get(id = 3)
    audio3 = Audio_store.objects.get(id = 4)
    audio4 = Audio_store.objects.get(id = 5)
    audio5 = Audio_store.objects.get(id = 6)
    context = {
        'audio1' : audio1,
        'audio2' : audio2,
        'audio3' : audio3,
        'audio4' : audio4,
        'audio5' : audio5,
    }
    return render(request, 'dictionnaire.html', context) 
