from django.core.management.base import BaseCommand
from recordatorios.utils import verificar_y_enviar_recordatorios

class Command(BaseCommand):
    help = 'Envía recordatorios automáticos de citas y vacunas'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Iniciando envío de recordatorios...'))
            verificar_y_enviar_recordatorios()
            self.stdout.write(self.style.SUCCESS('Recordatorios enviados con éxito'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al enviar recordatorios: {str(e)}'))