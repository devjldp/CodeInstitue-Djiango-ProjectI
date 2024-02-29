#  importa la función render desde el módulo shortcuts en el paquete django del framework Django para Python.
# La función render se utiliza comúnmente en las vistas de Django para renderizar plantillas HTML y devolver la respuesta al navegador del cliente. Proporciona una manera conveniente de generar una respuesta HTTP con contenido HTML basado en una plantilla y datos específicos del contexto.

from django.shortcuts import render, HttpResponse

# Necesito importar item para poder usarlos
from .models import Item


# Create your views here.

# Definición de una función de vista llamada 'say_hello' que toma el parámetro 'request'


def say_hello(request):
    # Devuelve una respuesta HTTP con el mensaje "Hello!"
    return HttpResponse("Hello!")

# Definición de una función de vista llamada 'get_todo_list' que toma el parámetro 'request'


def get_todo_list(request):
    # Creamos una nueva variable donde almacenaremos todos los items de la base de datos.
    items = Item.objects.all()
    # Creamos una nueva variable (dicionario) donde vamos a almacenar la variable.
    context = {
        'items': items
    }

    # Renderiza la plantilla 'todo/todo_list.html' utilizando la función 'render' y devuelve la respuesta
    return render(request, 'todo/todo_list.html', context)
