from django.contrib import admin
from django.urls import path
from GestorTareasApp import views

urlpatterns = [

    path('tareas/', views.tareas_general, name='Tareas_general'),
   
]