from django import forms
from .models import Propietario, Mascota, HistorialMedico, Vacuna

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'tipo', 'raza', 'color', 'fecha_nacimiento', 
                  'sexo', 'peso', 'propietario', 'notas']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        }

class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['mascota', 'motivo', 'diagnostico', 'tratamiento', 'notas']
        widgets = {
            'diagnostico': forms.Textarea(attrs={'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'rows': 3}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        }

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = ['mascota', 'nombre', 'fecha_aplicacion', 'fecha_proxima', 'notas']
        widgets = {
            'fecha_aplicacion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_proxima': forms.DateInput(attrs={'type': 'date'}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        }