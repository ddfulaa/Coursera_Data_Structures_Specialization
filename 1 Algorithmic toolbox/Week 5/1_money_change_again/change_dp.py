# Uses python3
import sys

def get_change(m):
    #write your code here
    minNumCoins=[0]
    coins=[1,3,4]
    for k in range(1,m+1):
        minNumCoins.append(float('inf'))
        for coin in coins:
            if k>=coin:
                numCoins=minNumCoins[k-coin]+1
                if numCoins< minNumCoins[k]:
                    minNumCoins[k]=numCoins
    return minNumCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
