# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    if left + 1 == right:
        if a[left]==a[right]:
            return a[left]
        else:
            return -1
    #write your code here
    punto_medio= (left+right)//2
    x=get_majority_element(a,left,punto_medio)
    y=get_majority_element(a,punto_medio+1,right) 
    if y!=-1:
        if a[left:right+1].count(y)>((right+1-left)//2):
            return y
    if x!=-1:
        if a[left:right+1].count(x)>((right+1-left)//2):
            return x
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
