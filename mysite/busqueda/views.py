from django.shortcuts import render
from django.http import HttpResponse
from personas import models
from django.apps import apps

def is_404(personas):
    if len(personas) == 0:
        return True

def Busqueda_view(request):
    lugar = request.GET.get('lugar', 'Ningún lugar')
    actividad = request.GET.get('actividad','Ninguna actividad')
    elementos = request.GET.lists()

    return HttpResponse('<h1> Hola Sirvió la vara: Lugar: ' + lugar +" Actividad: "+ actividad+ '</h1>')
# Create your views here.

def busqueda_persona(request):
    #Determinar lugar y Persona
    HTML_TEMPLATE = "paginabusqueda.html"
    SIN_LUGAR = 'Ningún lugar'
    SIN_ACTIVIDAD = 'Ninguna actividad'

    ModeloPersonas = apps.get_model('personas', 'PersonaModel')
    lugar = request.GET.get('lugar', SIN_LUGAR)
    actividad = request.GET.get('actividad',SIN_ACTIVIDAD)

    etiquetas_actividad = apps.get_model('personas', 'ActividadesActivasModel').objects.all()
    etiquetas_cantones = apps.get_model('personas', 'CantonesActivosModel').objects.all()
    datos = 'Esto es una prueba'

    personas = ModeloPersonas.objects.all()
    if is_404(personas):
        return render(request, '404-carrusel.html', { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})


    nombre = "nombre_debug"

    if lugar == None and actividad == None:
        return render(request, HTML_TEMPLATE, {'lugar':'sin lugar','personas':personas,'etiquetas_actividad':etiquetas_actividad, 'etiquetas_cantones': etiquetas_cantones})



    #Debe retornar siempre todos los cantones y todas las actividades productivas.
    #Si el lugar es todos.

    if lugar.lower() == 'todos' and actividad.lower() == 'todas':

        personas = ModeloPersonas.objects.all()
        if is_404(personas):
            return render(request, '404-carrusel.html', { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})

        imagenes_primera = personas[0].imagen_emprendimiento
        imagenes_resto = personas[1:len(personas)]
        nombre = personas[0].nombre
        ruta = personas[0].imagen_emprendimiento
        vector = []
        num = len(personas)
        vector = []
        for i in range(num):
            vector.append(i)
        return render(request, HTML_TEMPLATE, {'personas':personas,'datos': datos,'nombre':nombre ,'ruta':ruta,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector, 'etiquetas_actividad':etiquetas_actividad, 'etiquetas_cantones': etiquetas_cantones})

    elif lugar.lower() == 'todos':
        personas = ModeloPersonas.objects.filter(actividad = actividad)
        if is_404(personas):
            return render(request, '404-carrusel.html', { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})

        imagenes_primera = personas[0].imagen_emprendimiento
        imagenes_resto = personas[1:len(personas)]
        nombre = personas[0].nombre
        ruta = personas[0].imagen_emprendimiento
        vector = []
        num = len(personas)
        vector = []
        for i in range(num):
            vector.append(i)
        return render(request, HTML_TEMPLATE, {'personas':personas,'datos': datos,'nombre':nombre ,'ruta':ruta,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector,'etiquetas_actividad':etiquetas_actividad, 'etiquetas_cantones': etiquetas_cantones})

    elif actividad.lower() == 'todas':
        personas = ModeloPersonas.objects.filter(canton = lugar)
        if is_404(personas):
            return render(request, '404-carrusel.html', { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})


        imagenes_primera = personas[0].imagen_emprendimiento
        imagenes_resto = personas[1:len(personas)]
        nombre = personas[0].nombre
        ruta = personas[0].imagen_emprendimiento
        vector = []
        num = len(personas)
        vector = []
        for i in range(num):
            vector.append(i)
        return render(request, HTML_TEMPLATE, {'personas':personas,'datos': datos,'nombre':nombre ,'ruta':ruta,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector,'etiquetas_actividad':etiquetas_actividad, 'etiquetas_cantones': etiquetas_cantones})

    else:
        personas = ModeloPersonas.objects.filter(actividad = actividad).filter(canton = lugar)
        if is_404(personas):
            return render(request, '404-carrusel.html', { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})
        imagenes_primera = personas[0].imagen_emprendimiento
        imagenes_resto = personas[1:len(personas)]
        nombre = personas[0].nombre
        ruta = personas[0].imagen_emprendimiento
        vector = []
        num = len(personas)
        vector = []
        for i in range(num):
            vector.append(i)
        return render(request, HTML_TEMPLATE, {'personas':personas,'datos': datos,'nombre':nombre ,'ruta':ruta,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector,'etiquetas_actividad':etiquetas_actividad, 'etiquetas_cantones': etiquetas_cantones})

    #

        #imagenes = ImagenesModel.objects.all()
        #imagenes_primera = imagenes[0].imagen
        #imagenes_resto = imagenes[1:len(imagenes)]
        #num = len(imagenes)
        #vector = []
        #for i in range(num):
        #    vector.append(i)
        #return render(request, 'appimagenes/carrusel_pagina.html', {'imagenes':imagenes ,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector})

    return render(request, HTML_TEMPLATE, {'personas':personas, 'datos': datos, 'etiquetas_actividad':etiquetas_actividad, 'etiquetas_cantones': etiquetas_cantones})


def webpage_show(request):
    imagenes = ImagenesModel.objects.all()
    imagenes_primera = imagenes[0].imagen
    imagenes_resto = imagenes[1:len(imagenes)]
    num = len(imagenes)
    vector = []
    for i in range(num):
        vector.append(i)
    return render(request, 'appimagenes/carrusel_pagina.html', {'imagenes':imagenes ,'imagenesprimera': imagenes_primera,'imagenesresto': imagenes_resto, 'num': num, 'vector': vector})
