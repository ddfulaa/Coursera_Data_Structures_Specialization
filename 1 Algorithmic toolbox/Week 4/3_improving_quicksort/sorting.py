# Uses python3
import sys
import random
import datetime
def partition3(a, l, r):
    x = a[l]
    t = l
    s = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            t += 1
            a[i], a[t] = a[t], a[i]
        if a[i]==x:
            t +=1
            s +=1
            a[t],a[i] = a[i],a[t]
            a[t],a[s] = a[s],a[t]
    for i in range (0,s-l+1):
        a[s-i],a[t-i]=a[t-i],a[s-i]
    return (t-s+l,t)

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort_three_partition(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort_three_partition(a, l, m[0] - 1);
    randomized_quick_sort_three_partition(a, m[1] + 1, r);

def randomized_quick_sort_two_partition(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort_two_partition(a, l, m - 1);
    randomized_quick_sort_two_partition(a, m + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    begin_time=datetime.datetime.now()
    n, *a = list(map(int, input.split()))
    #begin_time=datetime.datetime.now()
    randomized_quick_sort_three_partition(a, 0, n-1)
    for x in a:
        print(x, end=' ')
    #print("\nTiempo de ejecucion:",datetime.datetime.now()-begin_time)
    
