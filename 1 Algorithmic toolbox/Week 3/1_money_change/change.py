# Uses python3
def get_change(m):
    #write your code here
    n=0
    for i in range(0,3):
        if m//10 > 0:
            n=n+ (m//10)
            m= m%10
        elif m//5 >0:
            n=n+(m//5)
            m=m%5
        else:
            n=n+m
            m=0
    return n

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
