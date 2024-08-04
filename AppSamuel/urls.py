from django.urls import path
from AppSamuel import views

urlpatterns = [
    path('', views.inicio, name='Inicio' ),
    path('', views.buscar_libros, name='BuscarLibros' ),
    path('autor/listar', views.AutorListView.as_view(), name='ListaAutores'),
    path('autor/nuevo',views.AutorCreateView.as_view(), name='NuevoAutor'),
    path('autor/<pk>',views.AutorDetailView.as_view(), name='DetalleAutor'),
    path('autor/<pk>/editar',views.AutorUpdateView.as_view(), name='EditarAutor'),
    path('autor/<pk>/borrar',views.AutorDeleteView.as_view(), name='BorrarAutor'),
]
