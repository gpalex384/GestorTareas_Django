from django.shortcuts import render
import requests as rq
import json
from GestorTareasApp.forms import Form_NuevaTarea

# Create your views here.

def tareas_general(request):
    
    url_get= "http://localhost:8080/products"
    response= rq.get(url_get).json()
    d= response[0]
    list_of_keys= d.keys()
    
    return render(request, "tareas_general.html", {"datos": response, "claves": list_of_keys})


def tareas_pendientes(request):

    return render(request, "tareas_pendientes.html")


def tareas_realizadas(request):

    return render(request, "tareas_realizadas.html")


def monitor(request):

    return render(request, "monitor.html")


def nueva_tarea(request):
    if request.method=="POST":
        miFormulario=Form_NuevaTarea(request.POST)

        if miFormulario.is_valid():
            url_post = "http://localhost:8080/products"
            # Almacenamos los datos introducidos en el formulario
            name = request.POST["nombre_producto"]
            price = request.POST["precio_producto"]

            # Pasamos la información a un diccionario, que identificamos como "data"
            data = {"name": name, "price": price}
            rq.post(url_post, json=data)
            return render(request, 'tarea_anyadida.html')
    
    else:
        miFormulario=Form_NuevaTarea()

    return render(request, "nueva_tarea_form.html", {'form': miFormulario})