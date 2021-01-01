# python3

#This implementation of Stack allow us to push, pop and find the maximum value in O(1)
class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximo = [float("-inf")]

    def Push(self, a):
        self.__stack.append(a)
        self.maximo.append(max(self.Max(),a))

    def Pop(self):
        assert(len(self.__stack))
        self.maximo.pop()
        return self.__stack.pop()

    def Max(self):
        #assert(len(self.__stack))
        return self.maximo[len(self.maximo)-1]
    
    def IsEmpty(self):
        return not bool(self.__stack)
#Implementation of a queue using two stacks
class QueueWithTwoStacks():
    #We need 2 stacks
    #Stack1 is used to enqueue and stack2 to dequeue
    def __init__(self):
        self.__stack1 = StackWithMax()
        self.__stack2 = StackWithMax()
    
    #check if stack2 is empty. In this case move all in stack1 to stack2, otherwise do nothing
    def checkStackTwo(self):
        if self.__stack2.IsEmpty():
            for i in range(len(self.__stack1._StackWithMax__stack)):
                self.__stack2.Push(self.__stack1.Pop())
    #Enqueue an element            
    def Enqueue(self, elemento):
        self.__stack1.Push(elemento)
        self.checkStackTwo()
    #Enqueue a list - the first element of the list is the first element to enter in the queue
    def ListEnqueue(self, lista):
        for elemento in lista:
            self.__stack1.Push(elemento)
        self.checkStackTwo()
    #Dequeue the first element in the list
    def Dequeue(self):
        self.checkStackTwo()
        if self.__stack2.IsEmpty():
            raise Exception("The operation cannot be done, because the queue is empty.")
        return self.__stack2.Pop()
    #check if the queue is empty
    def IsEmpty(self):
        self.checkStackTwo()
        return not bool(self.__stack2)
    #returns the max element in the queue
    def Max(self):
        return max(self.__stack1.Max(),self.__stack2.Max())
    #prints the queue as a list    
    def ImprimirCola(self):
        stack1=self.__stack1[:]
        stack2=self.__stack2[:]
        lista=[]
        print("ImprimirCola_Stack1",stack1._StackWithMax__stack)
        print("ImprimirCola_Stack2",stack2._StackWithMax__stack)
        for elemento in reversed(stack2._StackWithMax__stack):
            lista.append(elemento)
        for elemento in stack1._StackWithMax__stack:
            lista.append(elemento)
        print("Cola", lista)
        
        
        
def max_sliding_window_queue(sequence, m):
    q = QueueWithTwoStacks()
    q.ListEnqueue(sequence[0:m])
    maximums = [q.Max()]
    for i in range(m,len(sequence)):
        q.Enqueue(sequence[i])
        q.Dequeue()
        maximums.append(q.Max())
    return maximums

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums



if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window_queue(input_sequence, window_size))

