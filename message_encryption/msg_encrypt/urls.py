from django.contrib import admin
from django.urls import path
from msg_encrypt import views

urlpatterns = [
    path('', views.index, name='home'),
    path('encrypt', views.encrypt, name='encrypt'),
    path('decrypt', views.decrypt, name='decrypt'),
]