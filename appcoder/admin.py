from django.contrib import admin

# Register your models here.

from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre" , "comision")
    ordering = ("nombre",)
    
admin.site.register(Curso , CursoAdmin)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Profesor)

#Finalicé la práctica de la clase 20 , trabaje aplicando jazzmin y unfold con sus config , con las formas de ordenar las listas en el admin ,
#tambien creé un grupo , y repasé la etiqueta include de Dj , en views.py usé cursos = Curso.objects.all() para luego incluir un diccionario
#en el return(render) de cursos y pasar el contexto , y en cursos.html --> {{curso.nombre}}-{{curso.comision}} , dentro de un for.