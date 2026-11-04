from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Añade esta importación
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

# Vista personalizada para la raíz
def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirige a la página de inicio
    else:
        return redirect('login')

urlpatterns = [
    path('', root_redirect, name='root'),  # Cambiado
    path('admin/', admin.site.urls),
    path('citas/', include('citas.urls')),
    path('pacientes/', include('pacientes.urls')),
    # path('reportes/', include('reportes.urls')),  # Comenta esta línea si reportes no existe aún
    # path('recordatorios/', include('recordatorios.urls')),  # Comenta esta línea hasta que crees el archivo
    path('', include('autenticacion.urls')),
]