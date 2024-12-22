from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Curso

def crear_curso(request):
    nombre=input("Ingrese un nombre de curso:")
    comision=input("Ingrese un numero de comision:")
    curso = Curso(nombre=nombre,comision=comision)
    curso.save()
    texto = f"Curso registrado con éxito.  Curso:{curso.nombre} |||| Comision:{curso.comision}"
    return HttpResponse(texto)    
    
def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos":cursos}
    return render(request,"cursos.html",contexto)    

#Fin de la clase 18 , lo ultimo fue obtener datos de la DB y mostrarlos en el template con la funcion mostrar_cursos.

'''
Forma de hacer comentarios en mas de una linea
'''

def inicio(request):
    return render(request , "appcoder/inicio.html")

def estudiantes(request):
    return render(request , "appcoder/estudiantes.html")

def profesores(request):
    return render(request , "appcoder/profesores.html")

def entregables(request):
    return render(request , "appcoder/entregables.html")

#Hacer funcionar el css del template
