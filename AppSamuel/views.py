from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from AppSamuel.models import Autor, Libro, Categoria
from django.db.models import Q

def inicio(request):
    return render(request, 'AppSamuel/index.html')

def buscar_libros(request):
    query = request.GET.get('query', '')
    libros = Libro.objects.filter(titulo__icontains=query)
    autores = Autor.objects.filter(
    Q(nombre__icontains=query) | Q(apellido__icontains=query))
    categorias = Categoria.objects.filter(categoria__icontains=query)

    return render(request, 'AppSamuel/buscar_libros.html', {
        'query': query,
        'libros': libros,
        'autores': autores,
        'categorias': categorias
    })

# Vistas basadas en Clases - Autor
class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    context_object_name = "autores"
    template_name = "AppSamuel/autor_lista.html"

class AutorDetailView(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "AppSamuel/autor_detalle.html"

class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    template_name = "AppSamuel/autor_crear.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    template_name = "AppSamuel/autor_editar.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = "AppSamuel/autor_borrar.html"
    success_url = reverse_lazy("ListaAutores")

# Vistas basadas en Clases - Categoria
class CategoriaListView(LoginRequiredMixin, ListView):
    model = Autor
    context_object_name = "categorias"
    template_name = "AppSamuel/categoria_lista.html"

class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "AppSamuel/categoria_detalle.html"

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    template_name = "AppSamuel/categoria_crear.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    template_name = "AppSamuel/categoria_editar.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = "AppSamuel/categoria_borrar.html"
    success_url = reverse_lazy("ListaAutores")
