from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from pacientes.models import Vacuna
from citas.models import Cita
from .models import Recordatorio

def enviar_recordatorio_cita(cita):
    asunto = f'Recordatorio de Cita - Clínica Veterinaria'
    mensaje = f'''
    Estimado/a {cita.nombre_autorizado} {cita.apellido_autorizado},
    
    Le recordamos que tiene una cita programada para su mascota {cita.nombre_mascota} en nuestra clínica veterinaria.
    
    Detalles de la cita:
    - Fecha y hora: {cita.fecha.strftime('%d/%m/%Y a las %H:%M')}
    - Motivo: {cita.motivo}
    
    Por favor, llegue 10 minutos antes de la hora programada.
    Si necesita reprogramar o cancelar la cita, contáctenos lo antes posible.
    
    Saludos cordiales,
    Clínica Veterinaria
    '''
    
    # Enviar correo
    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,
        [cita.correo],
        fail_silently=False,
    )
    
    # Registrar el recordatorio
    recordatorio = Recordatorio(tipo='cita', cita=cita, enviado=True)
    recordatorio.save()
    
    return True

def enviar_recordatorio_vacuna(vacuna):
    propietario = vacuna.mascota.propietario
    mascota = vacuna.mascota
    
    asunto = f'Recordatorio de Vacuna - Clínica Veterinaria'
    mensaje = f'''
    Estimado/a {propietario.nombre} {propietario.apellido},
    
    Le recordamos que su mascota {mascota.nombre} tiene programada la siguiente vacuna:
    
    Detalles de la vacuna:
    - Vacuna: {vacuna.nombre}
    - Fecha programada: {vacuna.fecha_proxima.strftime('%d/%m/%Y')}
    
    Por favor, póngase en contacto con nosotros para programar una cita.
    
    Saludos cordiales,
    Clínica Veterinaria
    '''
    
    # Enviar correo
    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,
        [propietario.correo],
        fail_silently=False,
    )
    
    # Registrar el recordatorio
    recordatorio = Recordatorio(tipo='vacuna', vacuna=vacuna, enviado=True)
    recordatorio.save()
    
    return True

def verificar_y_enviar_recordatorios():
    hoy = timezone.now().date()
    manana = hoy + timedelta(days=1)
    
    # Recordatorios de citas para mañana
    citas_manana = Cita.objects.filter(
        fecha__date=manana,
        estado='CONFIRMADA'
    )
    
    for cita in citas_manana:
        # Verificar si ya se envió recordatorio
        if not Recordatorio.objects.filter(cita=cita, tipo='cita').exists():
            enviar_recordatorio_cita(cita)
    
    # Recordatorios de vacunas para próximos 7 días
    proxima_semana = hoy + timedelta(days=7)
    vacunas_proximas = Vacuna.objects.filter(
        fecha_proxima__gte=hoy,
        fecha_proxima__lte=proxima_semana
    )
    
    for vacuna in vacunas_proximas:
        # Verificar si ya se envió recordatorio
        if not Recordatorio.objects.filter(vacuna=vacuna, tipo='vacuna').exists():
            enviar_recordatorio_vacuna(vacuna)
    
    return True