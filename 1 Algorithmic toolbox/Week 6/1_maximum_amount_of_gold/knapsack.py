# Uses python3
import sys

def imprimirMatrix(M):
    for fila in M:
        print(fila)

def optimal_weight(W, w):
    # write your code here
    value = [[0] * (len(w)+1) for i in range(W+1)]
    #imprimirMatrix(value)
    for i in range(1,len(w)+1):
        for k in range(1,W+1):
            value[k][i]=value[k][i-1]
            if w[i-1]<=k:
                val=value[k-w[i-1]][i-1]+w[i-1]
                if value[k][i]<val:
                    value[k][i]=val
            #print(k,i)
            #imprimirMatrix(value)
    imprimirMatrix(value)
    return value[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
