from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from sentoki_project import settings 


urlpatterns = [
    path('', views.home_view, name='home'),
    path('interests',views.interests_view,name = 'interests'),
    path('matching',views.matching_view,name = 'matching'),
    path('profile',views.profile_view,name = 'profile'),
    path('mentors',views.mentors_view,name = 'mentors'),
]