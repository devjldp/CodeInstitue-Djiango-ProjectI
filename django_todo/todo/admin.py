# Importa la clase 'admin' del módulo 'django.contrib'
from django.contrib import admin

# Importa el modelo 'Item' desde el mismo directorio (puede ser ajustado según la estructura de tu proyecto)
from .models import Item

# Registra tus modelos aquí para que sean administrables en el panel de administración de Django

# Registra el modelo 'Item' en el panel de administración
admin.site.register(Item)
