from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista_libros),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('editar-libro/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('lista-libros/', views.lista_libros, name='lista_libros'),
     path('eliminar-libro/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),  
]