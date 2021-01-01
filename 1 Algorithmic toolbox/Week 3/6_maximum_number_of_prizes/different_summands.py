# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    i=1
    while n>=i:
        n=n-i
        summands.append(i)
        i +=1
    summands[i-2] += n
        
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
