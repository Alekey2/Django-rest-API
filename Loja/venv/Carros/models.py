from django.db import models
from uuid import uuid4

# Create your models here.

class Carros(models.Model):
    id_Carro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    cor = models.CharField(max_length=50)
    ano = models.IntegerField()
    estado = models.CharField(max_length=50)

    