from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.PersonaModel)
admin.site.register(models.ProvinciasActivasModel)
admin.site.register(models.CantonesActivosModel)
admin.site.register(models.DistritosActivosModel)
admin.site.register(models.ActividadesActivasModel)
