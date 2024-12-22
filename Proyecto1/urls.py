"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from Proyecto1.views import saludo , segunda_vista , diaDeHoy , miNombreEs , probandoTemplate , probando_cargadores 
from appcoder.views import crear_curso , mostrar_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/' , saludo) ,
    path('segunda_vista/' , segunda_vista),
    path('diaDeHoy/' , diaDeHoy),
    path('miNombreEs/<nombre>' , miNombreEs),   
    path('probandoTemplate/' , probandoTemplate),
    path('probando_cargadores/' , probando_cargadores),
    path('crear_curso/' , crear_curso),
    path('mostrar_cursos/' , mostrar_cursos),
    path("appcoder/" , include("appcoder.urls")),
]
