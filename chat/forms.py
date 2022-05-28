from django import forms 
from .models import *

class ChatForm(forms.ModelForm):
    class Meta:
        model=Chat
        fields=[
            'etudiant1',
            'etudiant2',
            'messages'
        ]