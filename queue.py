class Queue:
    def __init__(self,sizeOfQueue):
        self.l=[]
        self.sizeOfQueue=sizeOfQueue

    def enqueue(self,val):
        if not self.isFull():
            self.l.append(val)
        else:
            print("Queue is Full")
    def showQueue(self):
        return self.l
    def deque(self):
        if not self.isEmpty():
            self.l.pop(0)
        else:
            print("Queue is Empty")
    def peak(self):
        return self.l[0]
    def isFull(self):
        if len(self.l)==self.sizeOfQueue:
            return True
    def isEmpty(self):
        if len(self.l)==0:
            return True
ob=Queue(5)
ob.enqueue(1)
print(ob.showQueue())
ob.enqueue(2)
print(ob.showQueue())
ob.enqueue(3)
print(ob.showQueue())
ob.enqueue(4)
print(ob.showQueue())
ob.enqueue(5)
print(ob.showQueue())
ob.enqueue(6)
print(ob.peak())
ob.deque()
ob.deque()
ob.deque()
ob.deque()
ob.deque()
ob.deque()


