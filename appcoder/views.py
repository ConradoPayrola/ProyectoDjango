from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Curso,Profesor
from appcoder.forms import *
#Realizo la importacoón para las vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy

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

#Comienzo con la práctica de la clase 22.

#Arrancamos con el CRUD , comenzamos con READ.

def leerProfesores(request):
    
    profesores = Profesor.objects.all() #Traemos todos los profesores
    
    contexto = {"profesores":profesores}
    
    return render(request,"appcoder/leerProfesores.html",contexto) 

def profesorFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = ProfesorFormulario(request.POST) #aqui me llega toda la información del html
        
        print(miFormulario)
        
        if miFormulario.is_valid: #si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data
            
            profesor = Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            
            profesor.save()
            
            return render(request,"appcoder/inicio.html") #Vuelvo al inicio o a donde quiera
        
    else:
        
        miFormulario = ProfesorFormulario() #Formulario vacio para construir el html
        
    return render(request,"appcoder/profesorFormulario.html",{"miFormulario":miFormulario})      

def eliminarProfesor(request , profesor_nombre):
    
    #Recibe el nombre del profesor que vamos a eliminar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    #vuelvo al menu
    profesores = Profesor.objects.all() #traigo a todos los profesores para el contexto.
    
    contexto = {"profesores":profesores}
    
    return render(request , "appcoder/leerProfesores.html" , contexto)

def editarProfesor(request , profesor_nombre):
    
    #Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    
    #Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        
        miFormulario = ProfesorFormulario(request.POST) #Aqui me llega toda la informacion del html
        
        print(miFormulario)
        
        if miFormulario.is_valid: #Si pasa la validacion de Django
        
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            
            profesor.save()
            
            return render(request , "appcoder/inicio.html") #Vuelvo al inicio o otra pagina
        # En caso que no sea post
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email})
            
        #Voy al html que me permite editar
    return render(request , "appcoder/editarProfesor.html" , {"miFormulario":miFormulario , "profesor_nombre":profesor_nombre})    
        
#Lo último que hice de la práctica de la clase 22 , fue agregar la vista editarProfesor,
#lo siguiente es trabajar con las vistas basadas en clases.


#****************************VISTAS BASADAS EN CLASES************************************

#CLASE LISTVIEW : Para visualizar una lista de objetos.
class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appcoder/curso_lista.html"
    

#CLASE DETAILVIEW : Para visualizar un solo objeto.     
class CursoDetailView(DetailView):
    model = Curso
    template_name = "appcoder/curso_detalle.html"


#CLASE CREATEVIEW : Para crear objetos en la DB.
class CursoCreateView(CreateView):
    model = Curso
    template_name = "appcoder/curso_crear.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'comision']
    
    
#CLASE UPDATEVIEW : Para editar objetos de la DB.
class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "appcoder/curso_editar.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre' , 'comision']
    
    
#CLASE DELETEVIEW : Para eliminar un objeto de la DB.
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "appcoder/curso_borrar.html"
    success_url = reverse_lazy('ListaCursos')
    
    
    