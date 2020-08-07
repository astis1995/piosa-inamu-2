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
    HTML_TEMPLATE_INVITACION = "boot2/invitacion_busqueda.html" # invitacion_busqueda.html
    HTML_TEMPLATE = "boot2/paginabusqueda.html" # invitacion_busqueda.html
    #HTML_TEMPLATE = "paginabusqueda.html" # invitacion_busqueda.html
    HTML_TEMPLATE_404 = "404-carrusel.html" #
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
        return render(request, HTML_TEMPLATE_404, { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})


    nombre = "nombre_debug"

    if lugar == None and actividad == None:
        return render(request, HTML_TEMPLATE_404, {'lugar':'sin lugar','personas':personas,'etiquetas_actividad':etiquetas_actividad, 'etiquetas_cantones': etiquetas_cantones})



    #Debe retornar siempre todos los cantones y todas las actividades productivas.
    #Si el lugar es todos.
    if lugar == SIN_LUGAR and actividad == SIN_ACTIVIDAD: #Inicio
        return render(request, HTML_TEMPLATE_INVITACION, { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})

    if lugar.lower() == 'todos' and actividad.lower() == 'todas':

        personas = ModeloPersonas.objects.all()
        if is_404(personas):
            return render(request, HTML_TEMPLATE_404, { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})

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
            return render(request, HTML_TEMPLATE_404, { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})

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
            return render(request, HTML_TEMPLATE_404, { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})


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
            return render(request, HTML_TEMPLATE_404, { 'etiquetas_actividad': etiquetas_actividad, 'etiquetas_cantones':etiquetas_cantones})
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


from django.shortcuts import render
from django.http import HttpResponse
from personas import models
from django.apps import apps

def creador_matriz_dict_personas(personas):

    list1 = list(personas) #El queryset se convierte a una lista

    list2 =[]                 #Esta función devuelve una lista con diccionarions en donde está la persona, su fila y su columna
    fila = 0    #Empieza en la fila 0
    listaTemporal = []
    for elem in list1:
        indice = list1.index(elem)
        columna = indice % 3 #busca el indice del elemento modulo 3
        #Crea el diccionarions

        personaDict = {
        "persona": elem,
        "fila": fila,
        "columna": columna
        }
        #añade el diccionario a la lista2

        listaTemporal.append(personaDict)

        #si la columna es 2 el numero de fila aumenta.
        #Solo se pueden hasta 3 elementos en una fila
        #Se añade listaTemporal a lista2
        #Y se reinicia la listaTemporal

        if columna == 2:
            fila = fila + 1
            list2.append(listaTemporal)
            listaTemporal = []

        #Si el elemento es el último de la lista añade lo que haya
        if indice == len(list1)-1:
            list2.append(listaTemporal)

        #continúa con el siguiente elemento

    #Ahora se leerá el resultado
    return list2

    #fila_n = 0
    #columna = 0

    #for fila in list2:
    #    print("Fila")
    #    print(fila_n)
    #    for columna in fila:
    #        print(columna["persona"])
    #        print(columna["fila"])
    #        print(columna["columna"])
    #    fila_n= fila_n + 1

def is_404(personas):
    if len(personas) == 0:
        return True

def Busqueda_view(request):
    lugar = request.GET.get('lugar', 'Ningún lugar')
    actividad = request.GET.get('actividad','Ninguna actividad')
    elementos = request.GET.lists()

    return HttpResponse('<h1> Hola Sirvió la vara: Lugar: ' + lugar +" Actividad: "+ actividad+ '</h1>')
# Create your views here.
def perfiles_view_linear(request, pk_request):
    #Determinar lugar y Persona
    #HTML_TEMPLATE_INVITACION = "boot2/invitacion_busqueda.html" # invitacion_busqueda.html
    HTML_TEMPLATE = "perfil.html" # invitacion_busqueda.html
    HTML_TEMPLATE_404 = "404-carrusel.html" #
    UBICACION_MEDIA = "../../media/"
    datos = 'Esto es una prueba'

    #Si no se solicita ningún perfil se muestra una pagina de error
    if pk is None:
        return render(request, HTML_TEMPLATE_404)

    #Se carga el modelo de personas y lo filtra por pk
    ModeloPersonas = apps.get_model('personas', 'PersonaModel')
    perfiles = ModeloPersonas.objects.filter(pk = pk_request)


    #Convierte el QuerySet a lista

    return render(request, HTML_TEMPLATE, {"perfiles": perfiles, "prefijo": UBICACION_MEDIA})
