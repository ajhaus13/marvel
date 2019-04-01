from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_url'),
    path('', welcome, name='welcome_url'),
    path('api/', include('api.urls')),
    # path('character/', include('character.urls')),
]
