"""Imports"""
from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
]
