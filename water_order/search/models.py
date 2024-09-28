from django.db import models

# Create your models here.
# search/models.py (или orders/models.py)
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

