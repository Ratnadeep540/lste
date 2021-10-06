from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    
    path('diction/', views.diction,name="diction"),
    
]