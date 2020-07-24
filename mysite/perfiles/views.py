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

def perfiles_view(request):
    #Determinar lugar y Persona
    #HTML_TEMPLATE_INVITACION = "boot2/invitacion_busqueda.html" # invitacion_busqueda.html
    HTML_TEMPLATE = "temp_pic/index.html" # invitacion_busqueda.html
    HTML_TEMPLATE_404 = "404-carrusel.html" #
    UBICACION_MEDIA = "../../media/"
    datos = 'Esto es una prueba'

    #Se carga el modelo de personas.
    ModeloPersonas = apps.get_model('personas', 'PersonaModel')
    personas = ModeloPersonas.objects.all()

    #Si no hay perfiles muestra una pagina de error
    if is_404(personas):
        return render(request, HTML_TEMPLATE_404)

    #Convierte el QuerySet a lista
    #Define las columnas.
    lista_personas = list(personas)
    NUMERO_DE_COLUMNAS = 3

    #Crea una matriz de diccionarios cuyo contenido son las personas
    #sus filas y sus columnas
    matriz_perfiles = creador_matriz_dict_personas(personas)

    return render(request, HTML_TEMPLATE, {"matrizperfiles": matriz_perfiles, "prefijomedia": UBICACION_MEDIA})
