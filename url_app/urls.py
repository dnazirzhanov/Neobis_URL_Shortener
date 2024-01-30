from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:token>', views.home, name="Home"),
    path('', views.make, name="Make New")
]