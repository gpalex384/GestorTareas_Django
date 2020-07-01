from django import forms #Importamos la biblioteca 'forms'

class Form_NuevaTarea (forms.Form):

    """ CAMPOS DEL FORMULARIO DE TAREA NUEVA
    titulo_tarea = forms.CharField()
    descripcion_tarea = forms.CharField()
    proyecto_tarea = forms.CharField()
    fechaLimite_tarea = forms.DateField()"""

    # Producto nuevo (test)
    nombre_producto = forms.CharField()
    precio_producto = forms.DecimalField()
