"""
URL configuration for django_todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importando el módulo 'admin' del paquete 'django.contrib'
from django.contrib import admin
# Importando la función 'path' del paquete 'django.urls'
from django.urls import path

# # Importando la función 'say_hello' desde el módulo 'views' en el paquete 'todo'
# from todo.views import say_hello

from todo import views


# Definiendo las URL del proyecto
urlpatterns = [
    # Syntax path: path(route, view, kwargs=None, name=None)

    # Configurando la URL para acceder al panel de administración
    path('admin/', admin.site.urls),

    # Configurando la URL 'hello/' para activar la función 'say_hello'
    # y asignándole el nombre 'hello' para referenciarla más fácilmente
    # path('hello/', say_hello, name='hello'),

    # Esta es la homepage
    path('', views.get_todo_list, name='get_todo_list'),

    # Esta es la url para add un nuevo item
    path('add', views.add_item, name='add'),
    # esta es la url para editar un item
    path('edit/<item_id>', views.edit_item, name='edit'),
    # Esta es la url para toggle
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete')
]
