from django.shortcuts import render
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from citas.models import Cita
from pacientes.models import Mascota, HistorialMedico, Vacuna

@login_required
def dashboard(request):
    # Obtener la fecha actual
    hoy = timezone.now().date()
    inicio_semana = hoy - timedelta(days=hoy.weekday())
    fin_semana = inicio_semana + timedelta(days=6)
    
    # Estadísticas de citas
    total_citas = Cita.objects.count()
    citas_pendientes = Cita.objects.filter(estado='PENDIENTE').count()
    citas_hoy = Cita.objects.filter(fecha__date=hoy).count()
    citas_semana = Cita.objects.filter(fecha__date__range=[inicio_semana, fin_semana]).count()
    
    # Estadísticas de mascotas
    total_mascotas = Mascota.objects.count()
    mascotas_por_tipo = Mascota.objects.values('tipo').annotate(total=Count('id'))
    
    # Estadísticas de consultas médicas
    ultimas_consultas = HistorialMedico.objects.order_by('-fecha')[:5]
    
    # Estadísticas de vacunas
    proximas_vacunas = Vacuna.objects.filter(
        fecha_proxima__gte=hoy,
        fecha_proxima__lte=hoy + timedelta(days=30)
    ).order_by('fecha_proxima')[:10]
    
    # Construir contexto
    context = {
        'total_citas': total_citas,
        'citas_pendientes': citas_pendientes,
        'citas_hoy': citas_hoy,
        'citas_semana': citas_semana,
        'total_mascotas': total_mascotas,
        'mascotas_por_tipo': mascotas_por_tipo,
        'ultimas_consultas': ultimas_consultas,
        'proximas_vacunas': proximas_vacunas,
    }
    
    return render(request, 'reportes/dashboard.html', context)

@login_required
def reporte_citas(request):
    # Obtener parámetros de filtro
    estado = request.GET.get('estado', '')
    fecha_inicio_str = request.GET.get('fecha_inicio', '')
    fecha_fin_str = request.GET.get('fecha_fin', '')
    
    # Iniciar la consulta
    citas = Cita.objects.all()
    
    # Aplicar filtros si existen
    if estado:
        citas = citas.filter(estado=estado)
    
    if fecha_inicio_str:
        try:
            fecha_inicio = timezone.datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
            citas = citas.filter(fecha__date__gte=fecha_inicio)
        except ValueError:
            pass
    
    if fecha_fin_str:
        try:
            fecha_fin = timezone.datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()
            citas = citas.filter(fecha__date__lte=fecha_fin)
        except ValueError:
            pass
    
    # Estadísticas
    total_citas = citas.count()
    citas_por_estado = citas.values('estado').annotate(total=Count('id'))
    
    context = {
        'citas': citas.order_by('-fecha'),
        'total_citas': total_citas,
        'citas_por_estado': citas_por_estado,
        'estado_seleccionado': estado,
        'fecha_inicio': fecha_inicio_str,
        'fecha_fin': fecha_fin_str,
    }
    
    return render(request, 'reportes/reporte_citas.html', context)

@login_required
def reporte_pacientes(request):
    # Obtener parámetros de filtro
    tipo_animal = request.GET.get('tipo', '')
    
    # Iniciar la consulta
    mascotas = Mascota.objects.all()
    
    # Aplicar filtros si existen
    if tipo_animal:
        mascotas = mascotas.filter(tipo=tipo_animal)
    
    # Estadísticas
    total_mascotas = mascotas.count()
    mascotas_por_tipo = Mascota.objects.values('tipo').annotate(total=Count('id'))
    
    # Más estadísticas
    razas_comunes = Mascota.objects.values('raza').annotate(
        total=Count('id')
    ).order_by('-total')[:10]
    
    context = {
        'mascotas': mascotas.order_by('nombre'),
        'total_mascotas': total_mascotas,
        'mascotas_por_tipo': mascotas_por_tipo,
        'razas_comunes': razas_comunes,
        'tipo_seleccionado': tipo_animal,
    }
    
    return render(request, 'reportes/reporte_pacientes.html', context)

@login_required
def reporte_consultas(request):
    # Obtener parámetros de filtro
    fecha_inicio_str = request.GET.get('fecha_inicio', '')
    fecha_fin_str = request.GET.get('fecha_fin', '')
    
    # Iniciar la consulta
    consultas = HistorialMedico.objects.all()
    
    # Aplicar filtros si existen
    if fecha_inicio_str:
        try:
            fecha_inicio = timezone.datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
            consultas = consultas.filter(fecha__date__gte=fecha_inicio)
        except ValueError:
            pass
    
    if fecha_fin_str:
        try:
            fecha_fin = timezone.datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()
            consultas = consultas.filter(fecha__date__lte=fecha_fin)
        except ValueError:
            pass
    
    # Estadísticas
    total_consultas = consultas.count()
    consultas_por_motivo = consultas.values('motivo').annotate(
        total=Count('id')
    ).order_by('-total')[:10]
    
    context = {
        'consultas': consultas.order_by('-fecha'),
        'total_consultas': total_consultas,
        'consultas_por_motivo': consultas_por_motivo,
        'fecha_inicio': fecha_inicio_str,
        'fecha_fin': fecha_fin_str,
    }
    
    return render(request, 'reportes/reporte_consultas.html', context)

@login_required
def reporte_vacunas(request):
    # Obtener la fecha actual
    hoy = timezone.now().date()
    
    # Consultas
    vacunas_vencidas = Vacuna.objects.filter(fecha_proxima__lt=hoy).order_by('fecha_proxima')
    vacunas_proximas = Vacuna.objects.filter(
        fecha_proxima__gte=hoy,
        fecha_proxima__lte=hoy + timedelta(days=30)
    ).order_by('fecha_proxima')
    
    # Estadísticas
    total_vacunas = Vacuna.objects.count()
    vacunas_por_nombre = Vacuna.objects.values('nombre').annotate(
        total=Count('id')
    ).order_by('-total')[:10]
    
    context = {
        'vacunas_vencidas': vacunas_vencidas,
        'vacunas_proximas': vacunas_proximas,
        'total_vacunas': total_vacunas,
        'vacunas_por_nombre': vacunas_por_nombre,
        'hoy': hoy,
    }
    
    return render(request, 'reportes/reporte_vacunas.html', context)