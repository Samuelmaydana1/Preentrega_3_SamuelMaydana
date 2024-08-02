from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppSamuel.models import Autor

class AutorListView(ListView):
    model = Autor
    context_object_name = "autores"
    template_name = "vbc/autor_lista.html"

class AutorDetailView(DetailView):
    model = Autor
    template_name = "vbc/autor_detalle.html"

class AutorCreateView(CreateView):
    model = Autor
    template_name = "vbc/autor_crear.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class AutorUpdateView(UpdateView):
    model = Autor
    template_name = "vbc/autor_editar.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "vbc/autor_borrar.html"
    success_url = reverse_lazy("ListaAutores")

