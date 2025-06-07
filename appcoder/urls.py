from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("",inicio,name="inicio"),
    path("crear_curso/", cursos , name="cursos"),
    path("mostrar_cursos/",mostrar_cursos , name="mostrarCurso"),
    path("estudiantes/" , estudiantes , name="estudiantes"),
    path("profesores/" , profesores , name="profesores"),
    path("entregables/" , entregables , name="entregables"),
    path('form_con_api/', cursoFormulario , name="FormConApi"),
    path('busquedaCamada', busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar),
]   

#Debo hacer funcionar las etiquetas a utilizando la forma {% url 'nombre' %} en los href y utilizar nueva forma aqui en los path