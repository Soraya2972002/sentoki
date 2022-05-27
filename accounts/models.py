from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import BooleanField
import json


file = open('/home/ubuntu/Bureau/news/products/wilayas.json')
data = json.load(file)
WILAYAS_CHOICES = [('de',' ')]
for el in data :
    WILAYAS_CHOICES.append((el['name'],el['name']))
WILAYAS_CHOICES.append((" ",' '))


class CustomUser(AbstractUser):
    wilaya = models.CharField(max_length=100, choices = WILAYAS_CHOICES,default = 'def',blank = False, null = True)
    YEAR_CHOICES = [
        ('1cp', '1cp'),
        ('2cp', '2cp'),
        ('1cs', '1cs'),
        ('2cs', '2cs'),
        ('3cs', '3cs'),
    ]
    year = models.CharField(max_length=100, choices = YEAR_CHOICES, default= "1cp")
    email = models.EmailField(unique=True)
    image = models.ImageField(blank=True, upload_to='')
    computer_science = models.BooleanField(default = False)
    cyber_security = models.BooleanField(default = False)
    ai = models.BooleanField(default = False)
    design = models.BooleanField(default = False)
    it_systems = models.BooleanField(default = False)
    iot = models.BooleanField(default = False)
    software = models.BooleanField(default = False)
    data_science = models.BooleanField(default = False)
    networks = models.BooleanField(default = False)
    books = models.BooleanField(default = False)
    movies = models.BooleanField(default = False)
    music = models.BooleanField(default = False)
    signing = models.BooleanField(default = False)
    mangas = models.BooleanField(default = False)
    animes = models.BooleanField(default = False)
    series = models.BooleanField(default = False)
    drawing = models.BooleanField(default = False)
    hiking = models.BooleanField(default = False)
    football = models.BooleanField(default = False)
    tennis = models.BooleanField(default = False)
    cooking = models.BooleanField(default = False)
    basketball = models.BooleanField(default = False)
    handball = models.BooleanField(default = False)
    volleyball = models.BooleanField(default = False)
    fitness = models.BooleanField(default = False)
    jogging = models.BooleanField(default = False)
    cyclism = models.BooleanField(default = False)
