from django import forms

from accounts.models import CustomUser

class ImageUpdate(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image']
        