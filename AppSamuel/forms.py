from django import forms
from .models import Autor, Categoria, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categoria', 'fecha_de_publicacion']

class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)