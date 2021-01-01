def stringLargestSort(stringA,stringB):
    if stringA.startswith(stringB) or stringB.startswith(stringA):
        mini=min(stringA,stringB)
        maxi=max(stringA,stringB)
        x=stringLargestSort((maxi[len(mini):]),mini)
        if mini==x[0]:
            return [mini,maxi]
        else:
            return [maxi,mini]
    else:
        return [min(stringA,stringB),max(stringA,stringB)]
        
print(stringLargestSort("23","2"))