# Uses python3
import sys

#Idea: Suponer que se tiene una recta y se quiere poner marcas en ellas
#Hay tres marcas posibles; "l", "p" y "r", que significan respectivamente ser el inicio de un segmento,
# ser un punto normal y ser el fin de un segmento. Se escogieron los valores "l" "p" y "r", pues se debe respetar que
# "l"<"p"<"r". Podrían haber sido cualesquiera otras marcas que cumplan lo mismo, como 0,1,2 o "[",".","]" como si fueran los corchetes cuadrados .
# Luego vamos contando el número de corchetes que abrimos y faltan por cerrar y si se encuentra la marca de un punto se asigna el número de corchetes que falta por cerrar
# que conicide con el número de intervalos a los que pertence el punto
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts=list(zip(starts,["l"]*len(starts)))
    ends=list(zip(ends,["r"]*len(ends)))
    points=list(zip(points,["p"]*len(points),range(len(points))))
    recta=[]
    recta.extend(starts)
    recta.extend(ends)
    recta.extend(points)
    recta.sort()
    numero_corchetes=0
    for marca in recta:
        if marca[1]=="l":
            numero_corchetes +=1
        if marca[1]=="r":
            numero_corchetes-=1
        if marca[1]=="p":
            cnt[marca[2]]=numero_corchetes
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
