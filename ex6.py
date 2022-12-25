#string example

a="sakthi"
b='vel'
c=1
d=a+b+str(c)
print(d)


# int and float example

a=5
b=7.5
print(type(a))
print(type(b))
print(a)
print(b)
a=float(a)
b=int(b)
print(type(a))
print(type(b))
print(a)
print(b)


#example for boolean

x=2>2
y=(3==3)
print(x)
print(y)

#none datatype

a=None
print(a)
if a==0 or a=="":
    print("None is same as zer0 and None is same empty string")
else:
    print("None is not same as zero. None value is same as null which means empty")

#list example

a=[1,2.5,'a',"b"]
print(type(a))
print(a)
a[0]=-1
print(a)

#tuple example

a=(1,2.5,'a',"b")
print(type(a))
print(a)
#a[0]=-1 we can't change the tuple value after declaration
print(a[0])

#dictionary example

dic={1:'sakthi','a':"vel"}
print(dic)
print(dic[1])
dic['a']='M'
print(dic['a'])

#set example

s={1,2,3,'a','b','c',4,5}
#we can't access a item of a set using index value and key 
#it directly iterates throug items
print(s)
for j in s:
    print(j)
