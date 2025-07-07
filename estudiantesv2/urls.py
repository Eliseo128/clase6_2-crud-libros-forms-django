# estudiantes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('borrar/<int:id>/', views.borrar_estudiante, name='borrar_estudiante'),
]
