from django.urls import path
from AppSamuel import views

urlpatterns = [
    path('', views.inicio, name='Inicio' ),
    path('about', views.about, name='About'),
    path('autor/listar', views.AutorListView.as_view(), name='ListaAutores'),
    path('autor/nuevo',views.AutorCreateView.as_view(), name='NuevoAutor'),
    path('autor/<pk>',views.AutorDetailView.as_view(), name='DetalleAutor'),
    path('autor/<pk>/editar',views.AutorUpdateView.as_view(), name='EditarAutor'),
    path('autor/<pk>/borrar',views.AutorDeleteView.as_view(), name='BorrarAutor'),
    path('categoria/listar', views.CategoriaListView.as_view(), name='ListaCategorias'),
    path('categoria/nuevo',views.CategoriaCreateView.as_view(), name='NuevaCategoria'),
    path('categoria/<pk>',views.CategoriaDetailView.as_view(), name='DetalleCategoria'),
    path('categoria/<pk>/editar',views.CategoriaUpdateView.as_view(), name='EditarCategoria'),
    path('categoria/<pk>/borrar',views.CategoriaDeleteView.as_view(), name='BorrarCategoria'),
    path('libro/listar', views.LibroListView.as_view(), name='ListaLibros'),
    path('libro/nuevo',views.LibroCreateView.as_view(), name='NuevoLibro'),
    path('libro/<pk>',views.LibroDetailView.as_view(), name='DetalleLibro'),
    path('libro/<pk>/editar',views.LibroUpdateView.as_view(), name='EditarLibro'),
    path('libro/<pk>/borrar',views.LibroDeleteView.as_view(), name='BorrarLibro'),
]
