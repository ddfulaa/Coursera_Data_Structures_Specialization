def get_fibonacci_sum_squares(n):
    if (n == 0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        lista=list(range(3))
        lista[0]=0
        lista[1]=1
        for i in range(0,n):
            lista[2]=(lista[0]+lista[1])%10
            lista[0]=lista[1]
            lista[1]=lista[2]
        return (lista[0]*lista[1])%10

if __name__ == '__main__':
    n = int(input())
    #found a pattern in the numbers, just take n modulo 30
    print(get_fibonacci_sum_squares(n%30))
    