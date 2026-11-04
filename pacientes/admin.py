from django.contrib import admin

from django.contrib import admin
from .models import Propietario, Mascota, HistorialMedico, Vacuna

class MascotaInline(admin.TabularInline):
    model = Mascota
    extra = 0

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo')
    search_fields = ('nombre', 'apellido', 'telefono', 'correo')
    inlines = [MascotaInline]

class HistorialInline(admin.TabularInline):
    model = HistorialMedico
    extra = 0

class VacunaInline(admin.TabularInline):
    model = Vacuna
    extra = 0

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'raza', 'propietario')
    list_filter = ('tipo',)
    search_fields = ('nombre', 'raza', 'propietario__nombre', 'propietario__apellido')
    inlines = [HistorialInline, VacunaInline]

@admin.register(HistorialMedico)
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'fecha', 'motivo')
    list_filter = ('fecha',)
    search_fields = ('mascota__nombre', 'motivo', 'diagnostico')
    date_hierarchy = 'fecha'

@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'nombre', 'fecha_aplicacion', 'fecha_proxima')
    list_filter = ('fecha_aplicacion',)
    search_fields = ('mascota__nombre', 'nombre')
    date_hierarchy = 'fecha_aplicacion'