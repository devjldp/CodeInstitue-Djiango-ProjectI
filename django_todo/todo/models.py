# Import the models module from the Django database library
from django.db import models

# Define your models here.

# Create a model named 'Item'


class Item(models.Model):
    # Define a field 'name' as a character field with a maximum length of 50 characters
    name = models.CharField(max_length=50, null=False, blank=False)

    # Define a field 'done' as a boolean field with default value False
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        # Define una representación de cadena legible para el objeto Item
        return self.name
