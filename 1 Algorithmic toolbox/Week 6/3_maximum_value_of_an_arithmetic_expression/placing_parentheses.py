# Uses python3
def evalt(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def imprimirMatrix(M):
    for fila in M:
        print(fila)

def minMax(i,j,M,op):
    minimo=float('inf')
    maximo=float('-inf')
    for k in range(i,j):
        a=evalt(M[i][k],op[k],M[k+1][j])
        b=evalt(M[i][k],op[k],M[j][k+1])
        c=evalt(M[k][i],op[k],M[k+1][j])
        d=evalt(M[k][i],op[k],M[j][k+1])
        minimo=min(minimo,a,b,c,d)
        maximo=max(maximo,a,b,c,d)
    return (minimo,maximo)
        
def get_maximum_value(dataset):
    d=[]
    op=[]
    for i in range(len(dataset)):
        if i%2==0:
            d.append(int(dataset[i]))
        else:
            op.append(dataset[i])
    n=len(d)
    M = [[0] * (n) for i in range(n)]
    for i in range(n):
        M[i][i]=d[i]
    for s in range(n-1):
        for i in range(n-s-1):
            j=i+s+1
            aux=minMax(i,j,M,op)
            M[j][i]=aux[0]
            M[i][j]=aux[1]
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
