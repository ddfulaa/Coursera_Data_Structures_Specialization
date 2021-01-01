# python3
import sys


def compute_min_refills(distance, tank, stops):
    countStop=0
    acumm=0
    startPoint=0
    avanzar = False
    stops.append(distance)
    i=0
    while i < len(stops):
        while  (i<len(stops) and (stops[i]-startPoint)<=tank):
            avanzar=True
            i +=1
        if not avanzar:
            return -1
        elif stops[i-1]!=distance:
            countStop +=1
            startPoint = stops[i-1]            
            avanzar=False
        else:
            break
    return countStop

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split()) #stops es una lista
    print(compute_min_refills(d, m, stops))
