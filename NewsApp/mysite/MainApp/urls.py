from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('contact/', views.contact, name='contact'),
]