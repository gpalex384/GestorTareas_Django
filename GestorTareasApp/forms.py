from django import forms #Importamos la biblioteca 'forms'

class Form_NuevaTarea (forms.Form):

    # CAMPOS DEL FORMULARIO DE TAREA NUEVA
    titulo = forms.CharField(label="Título de la tarea: ")  # Campo obligatorio
    descripcion = forms.CharField(required=False, label="Descripción de la tarea: ")
    creado_por = forms.CharField(required=False, label="Tu nombre: ")
    responsable = forms.CharField(label="Responsable: ")    # Campo obligatorio

    """# Producto nuevo (test)
    nombre_producto = forms.CharField()
    precio_producto = forms.DecimalField()
    """
