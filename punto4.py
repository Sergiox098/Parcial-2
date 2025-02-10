#Desarrolar un algoritmo que calcule el promedio de un arreglo de reales.

floatlista = [1.2,-12,2342,0.009,-146,1]
floatlista2 = [1,4,-12,0.87,34,-14,5]
def promedioreal(x):
    sumaprom= 0
    tam = len(x)
    for i in x:
        sumaprom = sumaprom + i
    prom = sumaprom/tam
    return prom
print("El promedio de las listas con elementos reales es:",promedioreal(floatlista))
print("El promedio de las listas con elementos reales es:",promedioreal(floatlista2))