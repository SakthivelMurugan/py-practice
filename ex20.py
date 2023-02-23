# class grandparent:
#     a=10

#     def __init__(self):
#         self.n1=10
#         self.n2=10
#         print("i am superclass init")

#     def instanceMethod(self):
#         print(self.n1+self.n2)
#         print("hi sakthi")

#     @classmethod
#     def classMethod(cls):
#         cls.b=7
#         print(cls.b+cls.a)

#     @staticmethod
#     def __fun():
#         print("this is static method")

# class parent(grandparent):
#     # def __init__(self):
#     #     print("i am parent2 class")
#     def fun(self):
#         print("success")

# class child(parent):
#     def __init__(self):
#         super().__init__()

# ob2=child()
# ob2._grandparent__fun()



# ob=parent()
# ob.n1=(5)
# ob.instanceMethod()
# ob.fun()


# class method_overload:
#     def fun(self,b=None,c=None):
#         self.b=b
#         self.c=c
#         if self.b!=None and self.c!=None:
#             print((b+c)/2)
#         elif self.b!=None:
#             print(b*2)

#     def same(self):
#         print("i am parent")

# class child(method_overload):
#     def same(self):
#         print("i am me")

# ob=child()
# ob1=method_overload()
# ob1.same()

# class parent:
#     def __init__(self):
#         self.__name="sakthi"

#     def fun(self):
#         self.__a="success"
#         return self.__a
# ob=parent()
# print(ob._parent__name)

n=10
x=0
y=1
z=0
def fun(n,x,y,z):
    print(x)
    z=x
    x=x+y
    y=z
    n=n-1
    if n!=0:
        fun(n,x,y,z)
fun(n,x,y,z)



