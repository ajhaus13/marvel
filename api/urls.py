from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *
from character.views import character_info

urlpatterns = [
    path('', choose, name='choose_url'),
    path('character/', character_info,name='character_url'),
]