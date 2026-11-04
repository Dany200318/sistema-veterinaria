from django.db import models
from django.utils import timezone

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    direccion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Mascota(models.Model):
    TIPO_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Reptil', 'Reptil'),
        ('Otro', 'Otro'),
    ]
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    raza = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascotas')
    fecha_registro = models.DateTimeField(default=timezone.now)
    notas = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo} - {self.raza})"
    
    def edad(self):
        if self.fecha_nacimiento:
            today = timezone.now().date()
            return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return None

class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='historial')
    fecha = models.DateTimeField(default=timezone.now)
    motivo = models.CharField(max_length=200)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    notas = models.TextField(blank=True)
    
    def __str__(self):
        return f"Consulta de {self.mascota.nombre} el {self.fecha.strftime('%d/%m/%Y')}"

class Vacuna(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='vacunas')
    nombre = models.CharField(max_length=100)
    fecha_aplicacion = models.DateField()
    fecha_proxima = models.DateField(null=True, blank=True)
    notas = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.mascota.nombre} ({self.fecha_aplicacion})"