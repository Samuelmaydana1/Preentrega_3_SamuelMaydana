from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar_libros/', views.buscar_libros, name='buscar_libros'),
]
