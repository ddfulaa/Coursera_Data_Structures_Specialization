# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    n=len(weights)
    valuesPerWeight=[]
    for i in range(0,n):
        valuesPerWeight.append(values[i]/weights[i])
    listas=list(zip(valuesPerWeight,weights))
    listas.sort(reverse=True)
    for i in range(0,n):
        valuesPerWeight[i]=listas[i][0]
        weights[i]=listas[i][1]
    for i in range(0,n):
        if capacity==0:
            return value
        a=min(weights[i],capacity)
        value=value+a*valuesPerWeight[i]
        weights[i] = weights[i] - a
        capacity= capacity-a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
