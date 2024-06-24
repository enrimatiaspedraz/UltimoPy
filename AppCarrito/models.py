from django.db import models

# Create your models here.
class tablaProductos(models.Model):
    Código = models.CharField(primary_key=True, max_length=5)
    Producto = models.CharField(max_length=50)
    Cantidad = models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto = "({0}, ({1}))"
        return texto.format(self.Producto , self.Cantidad)