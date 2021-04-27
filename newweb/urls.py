from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('app/',views.app,name='app'),
path('contact/',views.contact,name='contact'),
path('terms/',views.terms,name='terms'),
path('careers/',views.careers,name='careers'),
]