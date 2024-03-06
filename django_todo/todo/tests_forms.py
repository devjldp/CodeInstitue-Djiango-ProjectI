from django.test import TestCase

from .forms import ItemForm

# Create your tests here.

from django.test import TestCase

# Importa la clase de formulario 'ItemForm' desde el módulo 'forms' en el mismo directorio.
from .forms import ItemForm

# Define una clase de pruebas llamada 'TestItemForm' que hereda de 'TestCase'.
class TestItemForm(TestCase):

    # Prueba que el campo 'name' en 'ItemForm' es obligatorio.
    def test_item_name_is_required(self):
        # Crea una instancia de 'ItemForm' con un diccionario que tiene un campo 'name' vacío.
        form = ItemForm({'name': ''})
        # Verifica que el formulario no sea válido cuando el campo 'name' está vacío.
        self.assertFalse(form.is_valid())
        # Verifica que haya un error asociado con el campo 'name'.
        self.assertIn('name', form.errors.keys())
        # Asegura que el mensaje de error para el campo 'name' sea "This field is required."
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # Prueba que el campo 'done' en 'ItemForm' no es obligatorio.
    def test_done_field_is_not_required(self):
        # Crea una instancia de 'ItemForm' con un nombre pero sin el campo 'done'.
        form = ItemForm({'name': 'Test Todo Item'})
        # Verifica que el formulario sea válido incluso sin el campo 'done'.
        self.assertTrue(form.is_valid())

    # Prueba que los campos especificados en la clase 'Meta' del formulario coinciden con los campos reales del formulario.
    def test_fields_are_explicit_in_form_metaclass(self):
        # Crea una instancia de 'ItemForm' sin datos.
        form = ItemForm()
        # Verifica que los campos especificados en la clase 'Meta' del formulario sean exactamente ['name', 'done'].
        self.assertEqual(form.Meta.fields, ['name', 'done'])
