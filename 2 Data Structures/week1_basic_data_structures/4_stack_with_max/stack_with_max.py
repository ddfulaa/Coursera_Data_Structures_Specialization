#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximo = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.maximo)==0:
            self.maximo.append(a)
        else:
            self.maximo.append(max(self.Max(),a))

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.maximo.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.maximo[len(self.maximo)-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
