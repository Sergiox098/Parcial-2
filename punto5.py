#Desarrollar un algoritmo que determine la mediana de un arreglo de enteros. La mediana es el numero que queda en la mitad del arreglo después de ser ordenado

medilista = [2,3,4,5,62,24,543,64,21,57,3412,53,1243,64,214,641,24,657,87,54,6578,6]
medilista2 = [1,2,3,4,5,6,7,8,9]

def mediana(x):
    tamano = len(x)
    medi = int(tamano/2)
    x.sort()
    print("La mediana de la lista",x, "es:",x[medi])
    

mediana(medilista)
mediana(medilista2)