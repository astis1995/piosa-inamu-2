def main():
    personas = ["juan","juan2","juan3","juan4","juan5","juan6","juan7","juan8","juan9","juan10","juan11"]
    
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
    fila_n = 0
    columna = 0
    
    for fila in list2:
        print("Fila") 
        print(fila_n)
        for columna in fila:
            print(columna["persona"])
            print(columna["fila"])
            print(columna["columna"])
        fila_n= fila_n + 1

if __name__ == "__main__":
    # execute only if run as a script
    main()
    
#sirve