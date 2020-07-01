from django.shortcuts import render
from django.http import HttpResponse
from personas import models
from django.apps import apps


def home_view(request):

    ModeloPersonas = apps.get_model('personas', 'PersonaModel')
    etiquetas_actividad = apps.get_model('personas', 'ActividadesActivasModel').objects.all()
    etiquetas_cantones = apps.get_model('personas', 'CantonesActivosModel').objects.all()

    personas = ModeloPersonas.objects.all()
    imagenes_primera = personas[0].imagen_emprendimiento
    imagenes_resto = personas[1:len(personas)]

    nombre = personas[0].nombre
    ruta = personas[0].imagen_emprendimiento
    return render(request, 'home.html',
    {'personas':personas,'nombre':nombre ,
    'ruta':ruta,'imagenesprimera': imagenes_primera,
    'imagenesresto': imagenes_resto,
    'etiquetas_actividad':etiquetas_actividad,
    'etiquetas_cantones': etiquetas_cantones})
