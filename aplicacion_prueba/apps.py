from django.apps import AppConfig


class AplicacionPruebaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicacion_prueba'

    def ready(self):
        import aplicacion_prueba.signals
