#Uses python3

import sys

def imprimirMatrix(M):
    for fila in M:
        print(fila)

 
    
def lcs2(a, b):
    #write your code here
    E = [[0] * (len(b)+1) for i in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                E[i][j]=E[i-1][j-1]+1
            else:
                E[i][j]=max(E[i-1][j],E[i][j-1])
    #imprimirMatrix(E)
    return E[len(a)][len(b)]

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

