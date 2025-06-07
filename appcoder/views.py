from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Curso
from appcoder.forms import CursoFormulario

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

def cursos(request):
    return render(request , "appcoder/cursos.html")

def estudiantes(request):
    return render(request , "appcoder/estudiantes.html")

def profesores(request):
    return render(request , "appcoder/profesores.html")

def entregables(request):
    return render(request , "appcoder/entregables.html")

#Hacer funcionar el css del template

#Ya pude solucionar tema css , solucionar error de subida de proyecto a GitHub.

#Prueba de edicion de archivo desde GitHub , para usar Git Pull

#Fin de la clase 19 hasta aqui , lo ultimo que hice de esa clase es subir el proyecto a GitHub.

#Ya comencé con la practica de la clase 20 , ya hice el template padre y heredé en inicio y agregué el bloque de contenido que cambia
#debo agregar funcionalidad a las etiquetas a del template padre.   

#Creo la vista para el formulario
def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'],comision=informacion['camada'])
            curso.save()
            return render(request,"appcoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request,"appcoder/formConApi.html",{"miFormulario":miFormulario})        
        

def busquedaCamada(request):
    return render(request,"appcoder/busquedaCamada.html")        

def buscar(request):
    if request.GET['camada']:
        
        camada=request.GET['camada']
        
        cursos=Curso.objects.filter(comision__icontains=camada)
        
        return render(request,"appcoder/resultadobusqueda.html",{"cursos":cursos,"camada":camada})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)    

#Terminé con toda la práctica de la clase 21 , pude hacer funcionar la vista y el formulario de busqueda en la base de datos , ahora la práctica
#de la clase 22.

