# students/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante

# Vista para Añadir y Mostrar Estudiantes
def agregar_y_mostrar(request):
    if request.method == 'POST':
        # Lógica para crear un nuevo estudiante
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validacion simple (en un proyecto real sería más robusta)
        if nombre and email and password:
            estudiante = Estudiante(nombre=nombre, email=email, password=password)
            estudiante .save()
        
        # Redirigir a la misma página para limpiar el formulario y mostrar la lista actualizada
        return redirect('agregar_y_mostrar')
    else:
        # Lógica para mostrar la lista de estudiantes
        lista_estudiantes = Estudiante.objects.all().order_by('id')
        context = {
            'estudiantes': lista_estudiantes
        }
        return render(request, 'alumnos/gestion_estudiantes.html', context)

# Vista para Editar Estudiantes
def editar_estudiante(request, estudiante_id):
    # Obtenemos el estudiante o mostramos un error 404 si no existe
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    
    if request.method == 'POST':
        # Actualizamos los datos con la información del formulario
        estudiante.nombre = request.POST.get('nombre')
        estudiante.email = request.POST.get('email')
        estudiante.password = request.POST.get('password')
        estudiante.save()
        return redirect('agregar_y_mostrar') # Redirigimos a la página principal
    
    # Si es GET, mostramos el formulario con los datos actuales del estudiante
    context = {
        'estudiante': estudiante
    }
    return render(request, 'alumnos/editar_estudiante.html', context)


# Vista para Borrar Estudiantes
def borrar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    if request.method == 'POST': # Aseguramos que la eliminación sea por POST
        estudiante.delete()
    return redirect('agregar_y_mostrar')