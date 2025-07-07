from django import forms

class CursoFormulario(forms.Form):
    #especifico los campos del formulario
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()  