from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("inicio/",inicio),
    path("crear_curso/",crear_curso),
    path("mostrar_cursos/",mostrar_cursos),
    path("estudiantes/" , estudiantes),
    path("profesores/" , profesores),
    path("entregables/" , entregables),
]
