from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza),
    path('login/', views.login),
    path('cadastrar/', views.cadastrar),

]
