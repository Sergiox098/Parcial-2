# Desarrolar un programa que determine sí en una lista no existen elementos repetidos
repelista = [0,1,2,3,4,5,6,2]
repelista2 = [98,65,4,23,23,43,54,65,54]

def repetir(x):
    norep=[]
    rep = []
    for i in x:
        if x.count(i) > 1:
            rep.append(i)
            if rep.count(i)>1:
                rep.remove(i)
        else:
            norep.append(i)
    print("Los siguientes elementos de la lista se repiten:",rep)
    print("Los siguientes elementos de la lista no se repiten:",norep)

repetir(repelista)
repetir(repelista2)
