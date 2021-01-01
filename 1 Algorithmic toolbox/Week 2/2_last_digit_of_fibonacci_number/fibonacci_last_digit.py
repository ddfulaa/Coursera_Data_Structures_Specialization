
def calc_fib_last_digit(n):
    if (n == 0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        lista=[0,1,0]
        for i in range(n-1):
            lista[2]=(lista[0]+lista[1])%10
            lista[0]=lista[1]
            lista[1]=lista[2]
        return lista[2]

n = int(input())
print(calc_fib_last_digit(n))