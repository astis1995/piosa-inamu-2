from django.db import models
from cms.models import CMSPlugin



class PerfilesPluginModel(CMSPlugin):

    def __str__(self):
        return "Perfiles"
