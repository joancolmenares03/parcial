def elementosRepetidos(lista1):
    aux = 0
    for x in lista1:
        if lista1.count(x) > 1:
            print(f"Hay elementos que se repiten en la lista")
            break
        else:
            aux +=1
    if aux == 0:
        print("No hay elementos que se repitan")
    
def vocalesContar(cadena):
    listaCadena = cadena.split()
    vocales = {"a","e","i","o","u"}
    print(listaCadena)
    aux = 0
    if cadena == None:
        print("No existe")
    else:
        for x in listaCadena:
            for i in vocales:
                if i in x:
                    aux += 1
                else:
                    continue
            if aux >= 2:
                print(x)
                aux = 0
            else:
                aux = 0



def comparador(lista1, lista2):
    listaDisyuncion = []
    for x in lista1:
        if lista2.count(x) == 0:
            listaDisyuncion.append(x)
        else:
            continue
    return print(listaDisyuncion)

def promedioArray(arreglo):
    
    x = 0
    for i in arreglo:         
        arreglo[arreglo.index(i)] = float(i)
    for i in arreglo:         
        x += i
    return print(x/len(arreglo))

def mediana(arreglo):
    ordenado = sorted(arreglo)
    if len(ordenado)%2 == 0:
        return print(ordenado[int((len(arreglo)/2)-1)])
    else:
        return print(ordenado[int((len(arreglo)/2))])

    
