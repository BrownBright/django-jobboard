from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('signup', views.signup ,name='signup'),
    path('profile', views.Profile ,name='profile'),
    path('profile/edit', views.profileedit ,name='profile_edit'),


]

