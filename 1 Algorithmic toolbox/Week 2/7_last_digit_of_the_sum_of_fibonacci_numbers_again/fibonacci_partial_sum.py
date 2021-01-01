# Uses python3

def get_fibonacci_partial_sum(m,n):
    if (n == 0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        lista=list(range(n+1))
        lista[0]=0
        lista[1]=1
        for i in range(2,n+1):
            lista[i]=(lista[i-1]+lista[i-2])%10
        #print(lista[m:n+1])
        return sum(lista[m:n+1])%10

if __name__ == '__main__':
    m,n = map(int, input().split())
    if (m%60)<=(n%60):
        print(get_fibonacci_partial_sum(m%60,n%60))
    else:
        print(get_fibonacci_partial_sum(m%60,60+n%60))
