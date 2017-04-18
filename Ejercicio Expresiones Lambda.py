from functools import reduce
def infoMatriz(matriz):
    
    apuestas= [list(filter(lambda i: i!=True and i!=False, i)) for i in matriz]
    gananciasBool= [list(filter(lambda i: i==True or i==False, i)) for i in matriz]
    promedio= [ reduce(lambda x,y: x+y, i)/len(i) for i in apuestas]
    promedioTotal= reduce(lambda x,y: x+y, promedio)/len(promedio) 

    g = list( map(lambda i,j: list(map(lambda a,b: a if (b) else 0, i, j)), apuestas, gananciasBool))
    ganancias= [reduce(lambda x,y: x+y, i) for i in g]

    mayorGanancia= max(ganancias)

    p=list( map(lambda i,j: list(map(lambda a,b: a if (not b) else 0, i, j)), apuestas, gananciasBool))
    perdidas= [reduce(lambda x,y: x+y, i) for i in p]

    mayorPerdida= max(perdidas)

    print("El promedio por jugador es:")
    print(promedio)
    print("El promedio total es:")
    print(promedioTotal)
    print("Las ganancias por jugador son:")
    print(ganancias)
    print("Las pérdidas por jugador son:")
    print(perdidas)
    print("La mayor ganancia fue de:")
    print(mayorGanancia)
    print("La mayor pérdida fue de:")
    print(mayorPerdida)

matriz= [[39, 36, 37, 38, 37,True,False,False,True],[49, 36, 37, 38, 37,True,False,False,True]]

infoMatriz(matriz)
