#Uses python3

import sys

def stringLargestSort(stringA,stringB):
    if (stringA.startswith(stringB) or stringB.startswith(stringA)) and (stringA != stringB) and stringA!="" and stringB!="":
        mini=min(stringA,stringB)
        maxi=max(stringA,stringB)
        x=stringLargestSort((maxi[len(mini):]),mini)
        if mini==x[0]:
            return [mini,maxi]
        else:
            return [maxi,mini]
    else:
        return [min(stringA,stringB),max(stringA,stringB)]
def largest_number(a):
    #write your code here
    res = ""
    ordenada=[]
    while a!=[]:
        maxi=""
        for x in a:
            maxi=stringLargestSort(maxi,x)[1]
        ordenada.append(maxi)
        a.remove(maxi)
    for x in ordenada:
        res=res+x           
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
