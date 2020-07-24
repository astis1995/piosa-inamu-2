from django.db import models
from cms.models import CMSPlugin



class CarruselPluginModel(CMSPlugin):

    def __str__(self):
        return "Plugin Carrusel"
