# Importa el módulo 'forms' de Django, que proporciona clases y funciones para trabajar con formularios.
from django import forms

# Importa la clase 'Item' del módulo 'models' en el mismo directorio (suponiendo que 'Item' es una clase de modelo definida en 'models.py').
from .models import Item


# Define una clase llamada 'ItemForm' que hereda de 'forms.ModelForm'.
class ItemForm(forms.ModelForm):
    # La clase 'Meta' proporciona metadatos asociados al formulario.
    class Meta:
        # Indica que este formulario está vinculado al modelo 'Item'.
        model = Item
        # Especifica los campos del modelo 'Item' que deben incluirse en el formulario.
        fields = ['name', 'done']
