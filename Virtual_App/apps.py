from django.apps import AppConfig


class VirtualAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Virtual_App'
