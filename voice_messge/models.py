from django.db import models

class Audio_store(models.Model):
    record = models.FileField(blank=True, upload_to='', default='media/vocal_test.aac')
