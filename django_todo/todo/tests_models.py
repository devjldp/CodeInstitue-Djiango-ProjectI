# Importa la clase TestCase del módulo django.test para crear pruebas unitarias
from django.test import TestCase

# Importa el modelo Item desde el directorio actual (usualmente es models.py)
from .models import Item

# Define y organiza las pruebas relacionadas con los modelos
class TestModels(TestCase):

    # Prueba para verificar que el atributo 'done' se establece como False por defecto
    def test_done_defaults_to_false(self):
        # Crea una instancia del modelo Item con el nombre especificado
        item = Item.objects.create(name="Test Todo Item")
        
        # Asegura que el atributo 'done' de la instancia sea False
        self.assertFalse(item.done)
    
    # Prueba para verificar que el método __str__ del modelo Item devuelve el nombre correcto
    def test_item_string_method_returns_name(self):
        # Crea una instancia del modelo Item con el nombre especificado
        item = Item.objects.create(name="Test Todo Item")
        
        # Verifica que el método __str__ devuelve el nombre correctamente
        self.assertEqual(str(item), "Test Todo Item")
