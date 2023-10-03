from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        
]

