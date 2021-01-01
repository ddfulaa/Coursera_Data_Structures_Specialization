# python3

import sys, threading

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.altura=self.compute_height_fast()
                
        #Naive implementation
        def compute_height(self):
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;
        def recursive_height(self,indice,tabla):
            if self.parent[indice]==-1:
                return 1
            if tabla[indice]==-1:
                tabla[indice]= self.recursive_height(self.parent[indice],tabla)+1
            return tabla[indice]
        def compute_height_fast(self):
            tabla=[-1]*self.n
            maximo=0
            for nodo in range(self.n):
                maximo=max(maximo,self.recursive_height(nodo,tabla))
            return maximo
            
def main():
  tree = TreeHeight()
  tree.read()
  #print(tree.compute_height())
  print(tree.altura)

threading.Thread(target=main).start()
