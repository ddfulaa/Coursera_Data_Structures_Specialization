# Uses python3
import sys
import itertools

def subsetSum(S, n, a, b, c, tabla):
    #Si tanto a, como b, como c son 0 es porque hemos llegado a una solución
    if a == 0 and b == 0 and c == 0:
        return 1
    # Caso base: No quedan elementos
    if n < 0:
        return 0
        
    entrada = (a, b, c, n)

    # si no hemos resuelto el subproblema, lo resolvemos y lo agreamos a la tabla para no tener que volver a calcularlo
    if entrada not in tabla:

        # Caso 1
        A = 0
        if a - S[n] >= 0:
            A = subsetSum(S, n - 1, a - S[n], b, c, tabla)

        # Caso 2
        B = 0
        if not A and (b - S[n] >= 0):
            B = subsetSum(S, n - 1, a, b - S[n], c, tabla)

        # Caso 3
        C = 0
        if (not A and not B) and (c - S[n] >= 0):
            C = subsetSum(S, n - 1, a, b, c - S[n], tabla)
        
        if A==1 or B==1 or C==1:
            tabla[entrada] = 1
        else:
            tabla[entrada] = 0
    
    return tabla[entrada]



def partition3(A):
    #Si hay menos de 3 elementos es imposible
    if len(A) < 3:
        return 0

    tabla = {}
    suma = sum(A)
    sumaParticion= suma //3   
    if suma%3 !=0:
        return 0
    return subsetSum(A, len(A) - 1, sumaParticion,sumaParticion,sumaParticion, tabla)




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

