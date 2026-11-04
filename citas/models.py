from django.db import models

class Cita(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    nombre_autorizado = models.CharField(max_length=100)
    apellido_autorizado = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    correo = models.EmailField()
    nombre_mascota = models.CharField(max_length=100)
    tipo_animal = models.CharField(max_length=20, choices=[
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ])
    raza = models.CharField(max_length=100)
    motivo = models.TextField()
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    
    def __str__(self):
        return f"Cita para {self.nombre_mascota} ({self.tipo_animal})"