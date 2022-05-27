from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    YEAR_CHOICES = [
        ('1cp', '1cp'),
        ('2cp', '2cp'),
        ('1cs', '1cs'),
        ('2cs', '2cs'),
        ('3cs', '3cs'),
    ]
    year = models.CharField(max_length=100, choices = YEAR_CHOICES, default= "1cp")
    email = models.EmailField(unique=True)