from django.http import HttpResponse
import datetime
from django.template import Template , Context , loader


def saludo(request):
    return HttpResponse("Hola Django")

def segunda_vista(request):
    return HttpResponse("<h1>Hola Django Framework</h1>")

def diaDeHoy(request):
    dia = datetime.datetime.now()  
    docDeTexto = f"Hoy es dia: {dia}"
    return HttpResponse(docDeTexto)
    
def miNombreEs(self , nombre):
    docDeTexto = f"Mi nombre es: <br><br>{nombre}"
    return HttpResponse(docDeTexto)

def probandoTemplate(request):
    
    nom = "Conrado"
    ape = "Payrola"
    lista_de_notas = 6 , 7 , 9 , 10 , 9
    diccionario ={"nombre":nom,"apellido":ape ,"notas":lista_de_notas}
    
    miHtml = open(r"C:\Users\conro\OneDrive\Documentos\CursoDesarrolloApps\Python\DjangoProyecto1\Proyecto1\plantillas\template1.html")
    plantilla = Template(miHtml.read())
    miHtml = Context()
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento) 

def probando_cargadores(request):
    
    nombre="Conrado"
    apellido="Payrola"
    diccionario={"nomb":nombre , "apell":apellido}
    
    plantilla = loader.get_template("template2.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

#Queda probar el cargador

