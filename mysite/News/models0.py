
# Create your models here.
from django.db import models
from cms.models import CMSPlugin
from polls.models import Poll
#Se debe importar los modelos de la aplicación que se quiere añadir.
#se debe importar la clase models de CMSPlugin
#Se deben importar los modelos de models para las bases de datos

class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.question
