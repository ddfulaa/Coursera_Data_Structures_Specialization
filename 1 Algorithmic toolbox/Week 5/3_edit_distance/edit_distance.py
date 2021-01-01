# Uses python3
def diff(s,t,i,j):
    if s[i-1]==t[j-1]:
        return 0
    else:
        return 1

def edit_distance(s, t):
    #write your code here
    E = [[0] * (len(t)+1) for i in range(len(s)+1)]
    for i in range(0,len(s)+1):
        E[i][0]=i
    for j in range(0,len(t)+1):
        E[0][j]=j
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            E[i][j]=min(E[i-1][j]+1,E[i][j-1]+1,E[i-1][j-1]+diff(s,t,i,j))
    return E[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
