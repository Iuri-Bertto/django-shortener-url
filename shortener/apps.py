from django.apps import AppConfig


class ShortenerConfig(AppConfig):
    name = 'shortener'
    verbose_name = 'shortener'
    label = 'shortener'

    def ready(self):
        import shortener.signals

