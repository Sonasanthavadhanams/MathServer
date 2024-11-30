from django.apps import AppConfig
from django.views.decorators.csrf import csrf_exempt

class MathsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mathsapp'
