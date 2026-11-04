from django.db import models
from django.utils import timezone
from pacientes.models import Mascota, Vacuna
from citas.models import Cita

class Recordatorio(models.Model):
    TIPO_CHOICES = [
        ('cita', 'Recordatorio de Cita'),
        ('vacuna', 'Recordatorio de Vacuna'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, null=True, blank=True, related_name='recordatorios')
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE, null=True, blank=True, related_name='recordatorios')
    fecha_envio = models.DateTimeField(default=timezone.now)
    enviado = models.BooleanField(default=False)
    
    def __str__(self):
        if self.tipo == 'cita':
            return f"Recordatorio de cita para {self.cita.nombre_mascota} el {self.cita.fecha.strftime('%d/%m/%Y')}"
        else:
            return f"Recordatorio de vacuna {self.vacuna.nombre} para {self.vacuna.mascota.nombre}"