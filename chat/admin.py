from django.contrib import admin
from .models import *

class ChatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chat,ChatAdmin)
