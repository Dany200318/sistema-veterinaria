from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Propietario, Mascota, HistorialMedico, Vacuna
from .forms import PropietarioForm, MascotaForm, HistorialMedicoForm, VacunaForm

# Vistas para Propietarios
def lista_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'pacientes/propietarios/lista.html', {'propietarios': propietarios})

def crear_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'pacientes/propietarios/form.html', {'form': form})

def editar_propietario(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'pacientes/propietarios/form.html', {'form': form})

def eliminar_propietario(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        propietario.delete()
        return redirect('lista_propietarios')
    return render(request, 'pacientes/propietarios/eliminar.html', {'propietario': propietario})

# Vistas para Mascotas
def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'pacientes/mascotas/lista.html', {'mascotas': mascotas})

def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    historial = mascota.historial.all().order_by('-fecha')
    vacunas = mascota.vacunas.all().order_by('-fecha_aplicacion')
    return render(request, 'pacientes/mascotas/detalle.html', {
        'mascota': mascota,
        'historial': historial,
        'vacunas': vacunas
    })

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'pacientes/mascotas/form.html', {'form': form})

def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'pacientes/mascotas/form.html', {'form': form})

def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('lista_mascotas')
    return render(request, 'pacientes/mascotas/eliminar.html', {'mascota': mascota})

# Vistas para Historial Médico
def crear_historial(request, mascota_id=None):
    mascota = None
    if mascota_id:
        mascota = get_object_or_404(Mascota, pk=mascota_id)
    
    if request.method == 'POST':
        form = HistorialMedicoForm(request.POST)
        if form.is_valid():
            historial = form.save()
            return redirect('detalle_mascota', pk=historial.mascota.id)
    else:
        initial = {}
        if mascota:
            initial = {'mascota': mascota}
        form = HistorialMedicoForm(initial=initial)
    
    return render(request, 'pacientes/historial/form.html', {'form': form})

def editar_historial(request, pk):
    historial = get_object_or_404(HistorialMedico, pk=pk)
    if request.method == 'POST':
        form = HistorialMedicoForm(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            return redirect('detalle_mascota', pk=historial.mascota.id)
    else:
        form = HistorialMedicoForm(instance=historial)
    return render(request, 'pacientes/historial/form.html', {'form': form})

def eliminar_historial(request, pk):
    historial = get_object_or_404(HistorialMedico, pk=pk)
    mascota_id = historial.mascota.id
    if request.method == 'POST':
        historial.delete()
        return redirect('detalle_mascota', pk=mascota_id)
    return render(request, 'pacientes/historial/eliminar.html', {'historial': historial})

# Vistas para Vacunas
def crear_vacuna(request, mascota_id=None):
    mascota = None
    if mascota_id:
        mascota = get_object_or_404(Mascota, pk=mascota_id)
    
    if request.method == 'POST':
        form = VacunaForm(request.POST)
        if form.is_valid():
            vacuna = form.save()
            return redirect('detalle_mascota', pk=vacuna.mascota.id)
    else:
        initial = {}
        if mascota:
            initial = {'mascota': mascota}
        form = VacunaForm(initial=initial)
    
    return render(request, 'pacientes/vacunas/form.html', {'form': form})

def editar_vacuna(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    if request.method == 'POST':
        form = VacunaForm(request.POST, instance=vacuna)
        if form.is_valid():
            form.save()
            return redirect('detalle_mascota', pk=vacuna.mascota.id)
    else:
        form = VacunaForm(instance=vacuna)
    return render(request, 'pacientes/vacunas/form.html', {'form': form})

def eliminar_vacuna(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    mascota_id = vacuna.mascota.id
    if request.method == 'POST':
        vacuna.delete()
        return redirect('detalle_mascota', pk=mascota_id)
    return render(request, 'pacientes/vacunas/eliminar.html', {'vacuna': vacuna})