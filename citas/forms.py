# En tu_app/forms.py
from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_autorizado', 'apellido_autorizado', 'celular', 'correo', 
                  'nombre_mascota', 'tipo_animal', 'raza', 'motivo', 'fecha', 'estado']
        widgets = {
            'fecha': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'motivo': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)
        # Convertir el widget de fecha a formato para input datetime-local
        if self.instance.fecha:
            self.initial['fecha'] = self.instance.fecha.strftime('%Y-%m-%dT%H:%M')