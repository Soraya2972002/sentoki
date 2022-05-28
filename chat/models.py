from datetime import datetime
from django.db import models
from django.forms import DateTimeField
import datetime

class Chat(models.Model):
    etudiant1 = models.TextField(max_length=20)
    etudiant2 = models.TextField(max_length=20)
    messages = models.TextField(max_length=200000000000000000000000000000000000000)
