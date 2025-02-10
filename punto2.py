#Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Sí la cadena existe debe imprimirla, y sí no existe debe imprimir no existe.

vocales = ["A","E","I","O","U","a","e","i","o","u"]
strlista = ["Casa","Agua","Hi","Programacion","Python","SSS",""]
strlista2 =[]
strlista3 = ["Arroz","NAda","Coche","Abuelos","Papaya","LA"]

def numvocales(x):
    mas =[]
    menos = []
    if len(x) == 0:
        print("La cadena no existe")
    else:
        for i in x:
            vocal = 0
            for j in i:
                for m in vocales:
                    if j == m:
                        vocal = vocal + 1
            if vocal >= 2:
                mas.append(i)
            if vocal < 2:
                menos.append(i)
        print("Las palabras de la lista que poseen más de dos vocales son:",mas)
        print("Las palabras de la lista que poseen menos de dos vocales son:",menos)
numvocales(strlista)
numvocales(strlista2)
numvocales(strlista3)