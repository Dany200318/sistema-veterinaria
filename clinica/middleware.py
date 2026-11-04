from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class RequireLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # URLs que no requieren autenticación
        self.exempt_urls = [
            '/login/',
            '/admin/login/',
            '/admin/'
        ]

    def __call__(self, request):
        # Comprobar si el usuario está autenticado
        if not request.user.is_authenticated:
            path = request.path_info
            
            # Permitir acceso a URLs exentas
            if any(path.startswith(url) for url in self.exempt_urls):
                return self.get_response(request)
            
            # Redirigir a login
            messages.warning(request, 'Debe iniciar sesión para acceder a esta página')
            return redirect(f'/login/?next={path}')
            
        return self.get_response(request)