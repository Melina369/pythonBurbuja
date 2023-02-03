def burbuja(arreglo):
    #longitud del arreglo
    long= len(arreglo)
    #recorrer el arreglo
    for i in range(long):
        #dentro del cilco, se vuelve a recorrer el arreglo, pero ahora hasta el penúltimo elemento
        #Sirve para que el indice_sig_elemento no de error
        for indice_actual in range(long-1):
            indice_sig_elemento = indice_actual + 1 #calcular
            if arreglo[indice_actual] > arreglo[indice_sig_elemento]:
                arreglo[indice_actual], arreglo[indice_sig_elemento] = arreglo[indice_sig_elemento], arreglo[indice_actual]

mi_arreglo = [4, 8, 7 , 1, 5, 14, 2, 73, 100, 82, 15, 90, 83, 102, 3]

print("\n================================")
print("Arreglo original: " , mi_arreglo)
print("Arreglo Ordenado: " )
burbuja(mi_arreglo)
print(mi_arreglo)

