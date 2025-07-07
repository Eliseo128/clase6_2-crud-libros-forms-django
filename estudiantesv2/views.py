# estudiantes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from .forms import EstudianteForm

def index(request):
    estudiantes = Estudiante.objects.all()
    form = EstudianteForm()

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'estudiantesv2/index.html', {
        'estudiantes': estudiantes,
        'form': form
    })

def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantesv2/editar.html', {
        'form': form,
        'estudiante': estudiante
    })

def borrar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('index')
