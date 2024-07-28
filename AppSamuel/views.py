from django.shortcuts import render, redirect
from .models import Autor, Categoria, Libro
from .forms import AutorForm, CategoriaForm, LibroForm, BuscarLibroForm

def inicio(request):
    return render(request, 'AppSamuel/inicio.html')

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_autor')
    else:
        form = AutorForm()
    return render(request, 'AppSamuel/agregar_autor.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'AppSamuel/agregar_categoria.html', {'form': form})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_libro')
    else:
        form = LibroForm()
    return render(request, 'AppSamuel/agregar_libro.html', {'form': form})

def buscar_libros(request):
    query = request.GET.get('query', '')
    libros = Libro.objects.filter(titulo__icontains=query)
    autores = Autor.objects.filter(nombre__icontains=query)
    categorias = Categoria.objects.filter(categoria__icontains=query)

    return render(request, 'AppSamuel/buscar_libros.html', {
        'query': query,
        'libros': libros,
        'autores': autores,
        'categorias': categorias
    })
