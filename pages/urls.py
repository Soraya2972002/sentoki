from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from sentoki_project import settings 


urlpatterns = [
    path('', views.home_view, name='home'),
    path('interests',views.interests_view,name = 'interests'),
    path('matching',views.matching_view,name = 'matching'),
    path('quizz',views.quizz,name = 'quizz'),
    path('classement',views.classement,name = 'classement'),
    path('dashboard',views.dashboard,name = 'dashboard'),
    path('galerie',views.galerie,name = 'galerie'),
    path('profile',views.profile,name = 'profile'),
    path('mentors',views.mentors,name = 'mentors'),
    path('culture',views.culture,name = 'culture'),
    path('personalities',views.personalities,name = 'personalities'),
    path('home2',views.home2,name = 'home2'),
    path('contact', views.contactus,name = 'contact'),
    path('messagerie', views.messagerie,name = 'messagerie')

]