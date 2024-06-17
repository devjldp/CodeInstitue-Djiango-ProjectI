# Importa la función render desde el módulo shortcuts en el paquete Django del framework Django para Python.
# La función render se utiliza comúnmente en las vistas de Django para renderizar plantillas HTML y devolver la respuesta al navegador del cliente.
# Proporciona una manera conveniente de generar una respuesta HTTP con contenido HTML basado en una plantilla y datos específicos del contexto.
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

# Necesito importar Item para poder usarlos
from .models import Item
# Importo la clase ItemForm
from .forms import ItemForm

# Definición de una función de vista llamada 'say_hello' que toma el parámetro 'request'
# def say_hello(request):
    # Devuelve una respuesta HTTP con el mensaje "Hello!"
    # return HttpResponse("Hello!")

# Definición de una función de vista llamada 'get_todo_list' que toma el parámetro 'request'


def get_todo_list(request):
    # Obtiene todos los items de la base de datos
    items = Item.objects.all()
    # Crea un diccionario de contexto con los items
    context = {
        'items': items
    }

    # Renderiza la plantilla 'todo/todo_list.html' utilizando la función 'render' y devuelve la respuesta
    # "context" se refiere a un conjunto de datos que se utiliza para pasar información desde la vista a la plantilla.
    return render(request, 'todo/todo_list.html', context)

# Definición de una función de vista llamada 'add_item' que toma el parámetro 'request'


def add_item(request):
    # Verifica si la solicitud es de tipo POST
    if request.method == 'POST':
        # Crea una instancia del formulario 'ItemForm' con los datos del formulario POST
        form = ItemForm(request.POST)
        # Verifica si el formulario es válido
        if form.is_valid():
            # Guarda el objeto Item en la base de datos
            form.save()
            # Redirige a la vista 'get_todo_list' después de agregar el elemento
            return redirect('get_todo_list')

    # Si la solicitud no es de tipo POST, crea una instancia de ItemForm
    form = ItemForm()
    # Crea un diccionario de contexto con el formulario
    context = {
        'form': form
    }
    # Renderiza la plantilla 'add_item.html' con el formulario como contexto
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)

    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')