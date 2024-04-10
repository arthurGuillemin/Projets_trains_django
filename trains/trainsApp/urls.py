
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index , name="index"),
    path('trains/detail/<int:trainsid>/', views.train_detail, name='train_detail'),
    path('trains/recherche/', views.recherche, name='recherche'),
    path('ajouter_train/', views.ajouter_train, name='ajouter_train'),  
    path('random/', views.random_train, name='random_train'),  





]
