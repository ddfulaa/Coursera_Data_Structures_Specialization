# Uses python3
import sys

def optimal_sequence(n):
    sequence = [n]
    numOperaciones = [0]
    operaciones = []
    #Primero calculamos el número mínimo de operaciones, como en el caso del cambio a monedas
    #Dependiendo de cual operacion es la que nos da el minimo, llenamos otra lista indicando la operacion que se hace para llegar a este número
    for i in range(1,n+1):
        numOperaciones.append(0)
        aux=[numOperaciones[i-1]+1,numOperaciones[i//2]+i%2+1,numOperaciones[i//3]+i%3+1]
        numOperaciones[i]=min(aux)
        if numOperaciones[i]==aux[0]:
            operaciones.append("+1")
        elif numOperaciones[i]==aux[1]:
            operaciones.append("*2")
        else:
            operaciones.append("*3")
    #Nos devolvemos en la lista de operaciones para saber de qué forma se obtiene el número indicado
    while n>1:
        if operaciones[n-1]=="+1":
            n=n-1
        elif operaciones[n-1]=="*2":
            n=n//2
        else:
            n=n//3
        sequence.append(n)
    sequence.reverse()
    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence)-1)
for x in sequence:
    print(x, end=' ')
