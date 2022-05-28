from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from sentoki_project import settings 


urlpatterns = [
    path('image', views.image_view, name = 'image_upload'),
    path('updateimage/<int:id>', views.updateimage, name = 'image_update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)