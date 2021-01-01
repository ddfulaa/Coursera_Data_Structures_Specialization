# Uses python3
def get_pisano_period(n,m):
    if (n == 0):
        return 0
    elif (n==1):
        return 0
    elif (n>1):
        lista=[0,1,0]
        count=0
        for i in range(n-1):
            lista[2]=(lista[0]+lista[1])%m
            lista[0]=lista[1]
            lista[1]=lista[2]
            count+=1
            if lista[0]==0 and lista[1]==1:
                return count
        return 0

def get_fibonacci_huge(n,m):
    if (n == 0):
        return 0
    elif (n==1):
        return 1
    elif (n>1):
        lista=list(range(n+1))
        lista[0]=0
        lista[1]=1
        for i in range(2,n+1):
            lista[i]=(lista[i-1]+lista[i-2])%m
        return lista[n]

if __name__ == '__main__':
    n, m = map(int, input().split())
    p=get_pisano_period(n,m)
    if (p==0):
        print(get_fibonacci_huge(n,m))
    else:
        print(get_fibonacci_huge(n%p,m))