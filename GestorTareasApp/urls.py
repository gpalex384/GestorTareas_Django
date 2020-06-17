from django.contrib import admin
from django.urls import path
from GestorTareasApp import views

urlpatterns = [

    path('tareas/', views.tareas_general, name='Tareas_general'),
    path('tareasPendientes/', views.tareas_pendientes, name='Tareas_pendientes'),
    path('tareasRealizadas/', views.tareas_realizadas, name='Tareas_realizadas'),
    path('monitor/', views.monitor, name='Monitor'),
   
]