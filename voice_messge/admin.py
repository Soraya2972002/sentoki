from django.contrib import admin
from .models import *

class AudioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Audio_store,AudioAdmin)
