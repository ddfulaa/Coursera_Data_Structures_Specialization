#Uses python3
import sys
import math
import random
#Para mayor legilibilidad del código se define la clase Punto
class Punto(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
#Calcula la distancia entres dos puntos        
def distancia(p,q):
    return math.sqrt((p.x-q.x)**2 + (p.y-q.y)**2)
    
#Imprime una lista de puntos    
def imprimir_puntos(P):
    for punto in P:
        print("(",punto.x,",",punto.y,")", end=" ")
    print("")
    return 0
    
#Función recursiva donde se aplica dividir y conquistar    
def dist_min_recursiva(Px, Py):
    n=len(Px)
    if n==2:
        #Calcule la distancia mínima entre los dos puntos
        return distancia(Px[0],Px[1])
    if n==3:
        #Calcule la distancia mínima entre los tres puntos
        return min(distancia(Px[0],Px[1]),distancia(Px[0],Px[2]),distancia(Px[2],Px[1]))
    im = n//2 #indice medio
    
    Py1=[] #Lista que guardará los puntos de la primera parte de la lista, pero ordenados con respecto a y
    Py2=[] #Lista que guardará los puntos de la segunda parte de la lista, pero ordenados con respecto a y
    
    for i in range(n):
        if Py[i].x < Px[im].x:
            Py1.append(Py[i])
        else:
            Py2.append(Py[i])
                        
    d1=dist_min_recursiva(Px[0:im],Py1)
    d2=dist_min_recursiva(Px[im:n],Py2)
    d=min(d1,d2)
    
    # Clasificamos los puntos dentro de la franja (pm.x-d,pm.x+d)
    franja=[]
    #la recta vertical que pasa por este punto es la que divide a los puntos
    coordenada_x_punto_medio=(Px[im].x + Px[im-1].x)/2
    
    #Se toman de Py para que queden ordenados respecto a y
    for punto in Py:
        if abs(punto.x - coordenada_x_punto_medio) < d:
            franja.append(punto)
    
    for i in range(len(franja)):
        for j in range(i+1,len(franja)):
            if franja[j].y - franja[i].y >= d:
                break
            if (distancia(franja[i],franja[j]) < d):
                d=distancia(franja[i],franja[j])
    return d
    
def distancia_minima(P):
    n=len(P)
    Px=P[:] #Lista que contiene los puntos ordenados con respecto a x
    Py=P[:] #Lista que contiene los puntos ordenados con respecto a y
    
    Px.sort(key= lambda punto: punto.x) #Ordene respecto a x
    Py.sort(key= lambda punto: punto.y) #Ordene respecto a y

    return dist_min_recursiva(Px,Py)


def fuerza_bruta(P):
    minimo=distancia(P[0],P[1])
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            minimo=min(minimo,distancia(P[i],P[j]))
    return minimo

def tester(k):
    P=[]
    for i in range(k):
        P.append(Punto(random.randint(-10**9,10**9),random.randint(-10**9,10**9)))
    #print("{0:.9f}".format(distancia_minima(P)))
    #print("{0:.9f}".format(fuerza_bruta(P)))
    if (distancia_minima(P)!=fuerza_bruta(P)):
        return P
    return []
if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #x = data[1::2]
    #y = data[2::2]
    #P=[]
    #for i in range(n):
        #P.append(Punto(x[i],y[i]))
        
    #Tester
    #print("{0:.9f}".format(distancia_minima(P)))
    #print("{0:.9f}".format(fuerza_bruta(P)))
    for i in range(1000):
        P=tester(50)
        if len(P)!=0:
            print(P)