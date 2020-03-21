from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoria',
        inique=True
    )

    def __str__(self):    #Cuando se carga categoria hace referencia a la descripción 
        return '{}'.format(self.descripcion)
        
    def save(self):
        self.descripcion = self.descripcion.upper() #Pongo la descripción en mayusculas
        super(Categoria, self).save() # Para guardarlo mando a traer el metodo save de la clase padre Categoria

    class Meta:
        verbose_name_plural = 'Categorias' #Guardo el nombre cuando se refriera a plural
