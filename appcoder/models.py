from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30 , null=True)
    comision = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()   
    
    def __str__(self):
        return self.nombre
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
#Pasé los modelos al admin de Dj y les agregué el método str para que en el admin figuren con su nombre propio y no como object() , y agregué registros a la db
#desde el admin