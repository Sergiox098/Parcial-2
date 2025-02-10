#Desarrollar un programa que dadas dos listas determine en qué elementos tiene la primera lista que no tenga la segunda lista.

lista1 = [1,2,3,4,5,6,7,8,9,0]
lista2 = [1,3,5,7,9]
lista3 = [2,4,6,8,0]

def comparar(x,y):
    poseer = []
    noposeer = []
    var = True
    if x == y:
        print("Las listas son iguales")
    else:
        for i in x:
            for j in y:
                if j ==i:
                    var = True
                    break
                else:
                    var = False
            if var == True:
                poseer.append(i)
            else:
                noposeer.append(i)
        print("La lista 2 posee los siguientes eleementos de la lista 1",poseer)
        print("La lista 2 no posee los siguientes eleementos de la lista 1",noposeer)

            
comparar(lista1,lista2)