# python3

from collections import namedtuple
import os
#This implementation of Stack allow us to push, pop and find the maximum value in O(1)
#You have to init this queue with a maximum size
class Stack():
    def __init__(self):
        self.__stack = []
        
    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        return self.__stack.pop()

    def StackLen(self):
        #assert(len(self.__stack))
        return len(self.__stack)
        
    def IsEmpty(self):
        return not bool(self.__stack)
#Implementation of a queue using two stacks
#This queue has a maximum size and have to be initialized
class QueueWithTwoStacks():
    #We need 2 stacks
    #Stack1 is used to enqueue and stack2 to dequeue, default value is 0
    def __init__(self, size=0):
        self.__stack1 = Stack()
        self.__stack2 = Stack()
        self.__maxsize = size    
    #check if stack2 is empty. In this case move all in stack1 to stack2, otherwise do nothing
    def checkStackTwo(self):
        if self.__stack2.IsEmpty():
            for i in range(len(self.__stack1._Stack__stack)):
                self.__stack2.Push(self.__stack1.Pop())
    def GetSize(self):
        return self.__stack1.StackLen()+self.__stack2.StackLen()
    def GetLastElement(self):
        self.checkStackTwo()
        if self.__stack2.IsEmpty():
            raise Exception("There is no last element because the queue is empty.")
        if self.__stack1.IsEmpty():
            return self.__stack2._Stack__stack[0]
        else:
            return self.__stack1._Stack__stack[len(self.__stack1._Stack__stack)-1]
            
    def GetFirstElement(self):
        self.checkStackTwo()
        if self.__stack2.IsEmpty():
            raise Exception("There is no last element because the queue is empty.")
        return self.__stack2._Stack__stack[len(self.__stack2._Stack__stack)-1]
    #Enqueue an element            
    def Enqueue(self, elemento):
        if self.GetSize()<self.__maxsize:
            self.__stack1.Push(elemento)
        else:
            return False
        self.checkStackTwo()
        return True
    #Dequeue the first element in the list
    def Dequeue(self):
        self.checkStackTwo()
        if self.__stack2.IsEmpty():
            raise Exception("The operation cannot be done, because the queue is empty.")
        return self.__stack2.Pop()
    #check if the queue is empty
    def IsEmpty(self):
        self.checkStackTwo()
        return self.__stack2.IsEmpty()
        
    #returns the max element in the queue
    #prints the queue as a list    
    def ImprimirCola(self, mensaje=""):
        stack1=self.__stack1._Stack__stack[:]
        stack2=self.__stack2._Stack__stack[:]
        lista=[]
        print(mensaje+"Stack1",stack1)
        print(mensaje+"Stack2",stack2)
        for elemento in reversed(stack2):
            lista.append(elemento)
        for elemento in stack1:
            lista.append(elemento)
        print(mensaje+"Cola", lista)

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = QueueWithTwoStacks(size)
    def GetSize(self):
        return self.size
    def process(self, request):
        # write your code here
        if self.finish_time.IsEmpty():
            self.finish_time.Enqueue(request.arrived_at+request.time_to_process)
            return Response(False,request.arrived_at)
        else:
            cont=self.finish_time.GetSize()
            for _ in range(cont):
                if request.arrived_at>=self.finish_time.GetFirstElement():
                    self.finish_time.Dequeue()
                else:
                    break
            if self.finish_time.GetSize()<self.GetSize():
                if self.finish_time.IsEmpty():
                    self.finish_time.Enqueue(request.arrived_at+request.time_to_process)
                    return Response(False,request.arrived_at)
                else:
                    beforethis=self.finish_time.GetLastElement()
                    self.finish_time.Enqueue(beforethis+request.time_to_process)
                    return Response(False,beforethis)
            else:
                return Response(True, -1)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    #Code for file tests
    """ 
    file="\\tests\\22"
    path=os.getcwd()+file
    f=open(path,"r")
    buffer_size, n_requests = map(int, f.readline().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, f.readline().split())
        requests.append(Request(arrived_at, time_to_process))
    f.close()
    file=file+".a"
    path=os.getcwd()+file
    f=open(path,"r")
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)
    for response in responses:
        if int(f.readline())!=response.started_at:
            print(False)
            break
    f.close()
    """
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    
    
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)
    
if __name__ == "__main__":
    main()
