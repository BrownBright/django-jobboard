from django.contrib import admin
from django.urls import path
from . import views

app_name = 'contact'


urlpatterns = [
    path('send-mail', views.send_me_mail ,name='send_mail'),
]