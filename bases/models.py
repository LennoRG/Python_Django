from django.db import models

from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) #Todo Objeto creado
    fc = models.TimeField(auto_now_add=True) #Fecha de creacion  o registro de Objeto
    fm = models.TimeField(auto_now=True) #Fecha de modificacion de objeto
    uc = models.ForeignKey(User, on_delete=models.CASCADE) #ClaseModelo mantiene una relacion de uno a muchos con User
    um = models.IntegerField(blank=True, null=True) #Usuario modifica, se permiten valores vacios y nulos

    class Meta:
        abstract=True
