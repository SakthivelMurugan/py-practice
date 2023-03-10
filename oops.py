# class parent:
#     a=10

#     def __init__(self):
#         self.n1=10
#         self.n2=10
#         print(self.n1+self.n2)

#     def instanceMethod(self):
#         print(self.n1+self.n2)
#         print("hi sakthi")

#     @classmethod
#     def classMethod(cls,b):
#         cls.b=b
#         print(cls.b+cls.a)


# ob=parent()
# ob.n1=5

# class parent:
#     agee=22
    
#     def __init__(self):
#         self.age=20
       
        
    
#     def fun(self,m):
#         self.m=m
    
#     def fun2(self):
#         print(self.m)
#         print(self.age)
# ob=parent()
# ob.fun(4)
# ob.fun2()
# print(ob.agee)


# class parent:
#     def __init__(self,name,age,dept):
#         self.name=name
#         self._age=age
#         self.__dept=dept

#     def update(self):
#         self.name="hi "+self.name
    
#     def show(self):
#         print(self.name)
#         print(self._age)
#         print(self.__dept)

# ob=parent("sakthi",22,"mca")
# ob._age=24
# ob._parent__dept="not"
# ob.update()
# ob.show()


string="abc123def456ghi678"
op=""
for i in range(len(string)):
    if (string[i]>='a' and string[i]<='z') or (string[i]>='A' and string[i]<='Z'):
        if i+1<len(string):
            if not((string[i+1]>='a' and string[i+1]<='z') or (string[i+1]>='A' and string[i+1]<='Z')):
                temp=""
                for j in range(len(string[:i+1])-1,-1,-1):
                    if (string[j]>='a' and string[j]<='z') or (string[j]>='A' and string[j]<='Z'):
                        temp+=string[j]
                    else:
                        break
                op+=temp
        elif i==len(string):
            temp=""
            for j in range(len(string[:i+1])-1,-1,-1):
                if (string[j]>='a' and string[j]<='z') or (string[j]>='A' and string[j]<='Z'):
                    temp+=string[j]
                else:
                    break
            op+=temp      
    else:
        op+=string[i]
print(op)