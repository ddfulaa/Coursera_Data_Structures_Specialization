# Uses python3
def calc_fib(n):
    if (n == 0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        lista=list(range(n+1))
        lista[0]=0
        lista[1]=1
        for i in range(2,n+1):
            lista[i]=lista[i-1]+lista[i-2]
        return lista[n]

n = int(input())
print(calc_fib(n))