def abs(n):
    if n>=0:
        return n
    else:
        return abs(-n)
    
def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)

def fibo(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return (fibo(a-1)+fibo(a-2))

def potenciacion(n,m):
    """n^m"""
    if m==0:
        return 1
    else:
        return n*potenciacion(n,m-1)

def multiplicacion(n,m):
    if m==0:
        return 0
    elif m==1:
        return n
    elif m>1:
        return n+multiplicacion(n,m-1)
    else:
        return -n+multiplicacion(n,m+1)
    
def dividir(n,m):
    if n<m:
        return 0
    else:
        return dividir(n-m,m)+1

def palindroma(palabra):
    if(len(palabra)-1<=0):
        return True
    if(palabra[0]!=palabra[len(palabra)-1]):
        return False
    else:
        return palindroma(palabra[1:len(palabra)-2])

def mcd(n,m):
    if m==0:
        return  n
    else:
        return mcd(m, n%m)

def suma(a):
    if a==0:
        return 0
    else:
        return (a%10+suma(a/10))


def convDecToBin(n):
    if n==1:
        return 1
    else:
        return ((convDecToBin(int(n/2)))*10)+n%2


def convBinToDec(n):
    if(n<2):
        return n
    else:
        return convBinToDec(int(n/10))*2+(n%10)


def invertir(lista):
    if(len(lista)-1<=0):
        return lista[len(lista)-1:len(lista)]
    else:
        return lista[len(lista)-1:len(lista)]+invertir(lista[0:len(lista)-1])

def menoresMultilistas(lista):
    if(lista[0]>lista[1]):
        if(len(lista)<=2):
            return lista[1]
        else:
            return menoresMultilistas(lista[1:])
    else:
        if(len(lista)<=2):
            return lista[0]
        else:
            return menoresMultilistas(lista[0:1]+lista[2:])

def listadelista(lista):
    if(len(lista)<=1):
        return [menoresMultilistas(lista[0])]
    else:
        return [menoresMultilistas(lista[0])]+listadelista(lista[1:len(lista)])

def contar(lista):
    if(len(lista)<=0):
        return 0
    for i in lista:
        if i[0] == 'J' or  i[0] == 'K' or  i[0] == 'Q':
            return 10+contar(lista[1:])
        elif i[0] == 'A':
            if(contar(lista[1:])+11>=21 or contar(lista[1:])+11<=21):
                return contar(lista[1:])+11
            else:
                return contar(lista[1:])+1
        else:
            return i[0]+contar(lista[1:])
        
lista = [[5,4],[20,5],['A',5],[1,5]]
print (contar(lista))

