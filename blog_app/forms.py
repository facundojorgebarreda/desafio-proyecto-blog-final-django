from django import forms
from .models import Publicacion, Categoria, Comentario

class FormularioPublicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'categoria']

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre_autor', 'contenido']
