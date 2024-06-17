# Importa la clase TestCase del módulo django.test para crear pruebas unitarias
from django.test import TestCase

# Importa el modelo Item desde el directorio actual (usualmente es models.py)
from .models import Item

# Define y organiza las pruebas relacionadas con las vistas
class TestViews(TestCase):

    # Prueba para verificar el acceso a la lista de tareas ('/')
    def test_get_todo_list(self):
        # Realiza una solicitud GET a la ruta '/'
        response = self.client.get('/')
        
        # Verifica que la solicitud sea exitosa (código de estado HTTP 200)
        self.assertEqual(response.status_code, 200)
        
        # Verifica que se use la plantilla 'todo/todo_list.html' para renderizar la respuesta
        self.assertTemplateUsed(response, "todo/todo_list.html")

    # Prueba para verificar el acceso a la página para agregar un ítem ('/add')
    def test_get_add_item_page(self):
        # Realiza una solicitud GET a la ruta '/add'
        response = self.client.get('/add')
        
        # Verifica que la solicitud sea exitosa (código de estado HTTP 200)
        self.assertEqual(response.status_code, 200)
        
        # Verifica que se use la plantilla 'todo/add_item.html' para renderizar la respuesta
        self.assertTemplateUsed(response, "todo/add_item.html")

    # Prueba para verificar el acceso a la página para editar un ítem específico ('/edit/<item.id>')
    def test_get_edit_item_page(self):
        # Crea una instancia del modelo Item con el nombre especificado
        item = Item.objects.create(name="Test Todo Item")
        
        # Realiza una solicitud GET a la ruta '/edit/<item.id>'
        response = self.client.get(f'/edit/{item.id}')
        
        # Verifica que la solicitud sea exitosa (código de estado HTTP 200)
        self.assertEqual(response.status_code, 200)
        
        # Verifica que se use la plantilla 'todo/edit_item.html' para renderizar la respuesta
        self.assertTemplateUsed(response, "todo/edit_item.html")

    # Prueba para verificar la capacidad de agregar un ítem mediante POST a la ruta '/add'
    def test_can_add_item(self):
        # Realiza una solicitud POST a la ruta '/add' con datos de formulario {'name': 'Test Added Item'}
        response = self.client.post('/add', {'name': 'Test Added Item'})
        
        # Verifica que la solicitud redireccione al '/' (código de estado HTTP 302)
        self.assertRedirects(response, '/')
    
    # Prueba para verificar la capacidad de eliminar un ítem mediante GET a la ruta '/delete/<item.id>'
    def test_can_delete_item(self):
        # Crea una instancia del modelo Item con el nombre especificado
        item = Item.objects.create(name="Test Todo Item")
        
        # Realiza una solicitud GET a la ruta '/delete/<item.id>'
        response = self.client.get(f'/delete/{item.id}')
        
        # Verifica que la solicitud redireccione al '/' (código de estado HTTP 302)
        self.assertRedirects(response, '/')
        
        # Verifica que el ítem ya no exista en la base de datos
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    # Prueba para verificar la capacidad de cambiar el estado de done de un ítem mediante GET a la ruta '/toggle/<item.id>'
    def test_can_toggle_item(self):
        # Crea una instancia del modelo Item con el nombre especificado
        item = Item.objects.create(name="Test Todo Item")
        
        # Realiza una solicitud GET a la ruta '/toggle/<item.id>'
        response = self.client.get(f'/toggle/{item.id}')
        
        # Verifica que la solicitud redireccione al '/' (código de estado HTTP 302)
        self.assertRedirects(response, '/')
        
        # Obtiene el ítem actualizado desde la base de datos y verifica que 'done' sea False
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    # Prueba para verificar la capacidad de editar un ítem mediante POST a la ruta '/edit/<item.id>'
    def test_can_edit_item(self):
        # Crea una instancia del modelo Item con el nombre especificado
        item = Item.objects.create(name="Test Todo Item")
        
        # Realiza una solicitud POST a la ruta '/edit/<item.id>' con datos de formulario {'name': 'Updated Name'}
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        
        # Verifica que la solicitud redireccione al '/' (código de estado HTTP 302)
        self.assertRedirects(response, '/')
        
        # Obtiene el ítem actualizado desde la base de datos y verifica que el nombre se haya actualizado correctamente
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
