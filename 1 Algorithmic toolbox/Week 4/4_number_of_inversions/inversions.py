# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        if right-left==1:
            if a[left]>a[left+1]:
                a[left],a[left+1]=a[left+1],a[left]
                number_of_inversions+=1
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
    #write your code here
    b1=a[left:ave+1]
    b2=a[ave+1:right+1]
    c=[]
    while len(b1)>0 and len(b2)>0:
        if b1[0] <= b2[0]:
            c.append(b1[0])
            b1.remove(b1[0])
        else:
            number_of_inversions +=len(b1)
            c.append(b2[0])
            b2.remove(b2[0])
    c.extend(b1)
    c.extend(b2)
    for i in range(len(c)):
        a[left+i]=c[i]
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
