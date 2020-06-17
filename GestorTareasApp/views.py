from django.shortcuts import render
import requests as rq
import json

# Create your views here.

def tareas_general(request):
    
    url= "http://localhost:8080/products"
    response= rq.get(url).json()
    d= response[0]
    list_of_keys= d.keys()
    
    
    return render(request, "tareas_general.html", {"datos": response, "claves": list_of_keys})