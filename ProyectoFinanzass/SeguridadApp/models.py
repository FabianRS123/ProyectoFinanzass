from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length=191, unique=True)
    email = models.EmailField(max_length=191, unique=True)
    direccion = models.CharField(max_length=50)
    ruc_dni = models.CharField(max_length=8, unique=True)
    estado = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'usuarios'  # Cambia el nombre de la tabla
