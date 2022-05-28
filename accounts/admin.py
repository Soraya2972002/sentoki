from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class EmailRequiredMixin(object):
    def __init__(self, *args, **kwargs):
        super(EmailRequiredMixin, self).__init__(*args, **kwargs)
        # make user email field required
        self.fields['email'].required = True
        #self.fields['num'].required = True

class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass


class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'year','image','wilaya',"computer_science","cyber_security",
        "ai","it_systems","iot","software","data_science","networks","books","movies","music","signing","mangas","animes","series","drawing","hiking","football","tennis","cooking","basketball",'handball',"volleyball","fitness","jogging",'cyclism',"gender","note_quizz","id_conv"
        )
    fieldsets = (
        (None, {
            'fields': ('username',),'classes': ('wide',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','year','image','wilaya',"computer_science","cyber_security",
        "ai","it_systems","iot","software","data_science","networks","books","movies","music","signing","mangas","animes","series","drawing","hiking","football","tennis","cooking","basketball",'handball',"volleyball","fitness","jogging",'cyclism','gender',"note_quizz","id_conv"),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2'),'classes': ('wide',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','year','image','wilaya',"computer_science","cyber_security",
        "ai","it_systems","iot","software","data_science","networks","books","movies","music","signing","mangas","animes","series","drawing","hiking","football","tennis","cooking","basketball",'handball',"volleyball","fitness","jogging",'cyclism','gender',"note_quizz","id_conv")
        }),
        
    )
    form = UserChangeForm
    add_form = UserCreationForm

admin.site.register(CustomUser, CustomUserAdmin)
