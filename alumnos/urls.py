# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para mostrar el listado y agregar estudiantes (Create y Read)
    path('', views.agregar_y_mostrar, name='agregar_y_mostrar'),
    
    # Ruta para borrar un estudiante (Delete)
    # Usamos POST para la eliminación por seguridad
    path('borrar/<int:estudiante_id>/', views.borrar_estudiante, name='borrar_estudiante'),

    # Ruta para editar un estudiante (Update)
    path('editar/<int:estudiante_id>/', views.editar_estudiante, name='editar_estudiante'),
]