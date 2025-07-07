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
    path('leerProfesores/', leerProfesores , name="LeerProfesores"),
    path('profesorFormulario/' , profesorFormulario , name="ProfesorFormulario"),
    path('eliminarProfesor/<profesor_nombre>/' , eliminarProfesor , name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/' , editarProfesor , name="EditarProfesor"),
    path('cursos/lista' , CursoListView.as_view() , name="ListaCursos"),
    path('cursos/nuevo' , CursoCreateView.as_view() , name="NuevoCurso"),
    path('cursos/<pk>' , CursoDetailView.as_view() , name="DetalleCurso"),
    path('cursos/<pk>/editar' , CursoUpdateView.as_view() , name="EditarCurso"),
    path('cursos/<pk>/borrar' , CursoDeleteView.as_view() , name="BorrarCurso"),
]   

#Debo hacer funcionar las etiquetas a utilizando la forma {% url 'nombre' %} en los href y utilizar nueva forma aqui en los path
