from django import forms

class CursoFormulario(forms.Form):
    #especifico los campos del formulario
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    
    