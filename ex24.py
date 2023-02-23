class className:
    def __init__(self):
        self.l=[]
    def push(self,val):
        self.val=val
        self.l.append(self.val)
    def terminate(self,indexvalue):
        self.indexvalue=indexvalue
        self.l.pop(self.indexvalue)
    def removelast(self):
        self.l.pop()
    def modify(self,modifyindex,v):
        self.modifyindex=modifyindex
        self.v=v
        self.l[self.modifyindex]=self.v
    def show(self):
        print(self.l)
ob=className()
ob.push(5)
ob.push(6)
ob.push(8)
ob.push(9)
ob.show()
ob.terminate(3)
ob.show()
ob.removelast()
ob.show()
ob.modify(1,7)
ob.show()


