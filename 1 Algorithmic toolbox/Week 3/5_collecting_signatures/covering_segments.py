# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    #print(segments)
    segments.sort()
    #print(segments)
    i=0
    aux_list1=[]
    aux_list2=[]
    maximo=segments[0][1]
    for s in segments:
        #print(max)
        if s[0]<= maximo:
            maximo=min(maximo,s[1])
            aux_list1.append(s)
        else:
            aux_list2.append(aux_list1)
            aux_list1=[s]
            maximo=s[1]
        #print(aux_list1)
    aux_list2.append(aux_list1)
    #print(aux_list2)
    for sublista in aux_list2:
        maximo=0
        for s in sublista:
            maximo=max(maximo,s[0])
        points.append(maximo)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
