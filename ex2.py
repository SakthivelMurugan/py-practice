#append
week = ["sunday","monday","tuesday","wenesday","thursday","friday","staturday"]
week.append("jan")
print(week)
#append list inside list
a = ["sunday","monday"]
b = ["tuesday","wednesday"]
a.append(b)
print(a)
#clear
x=["tuesday","wednesday"]
x.clear()
print(x)
#copy
c=a.copy()
print(c)
#count string
p=week.count("monday")
print(p)
#count number
s=[121,321,231,121,3131,125,121,412,121,1421,112]
d=s.count(121)
print(d)
#extend string
week.extend(a)
print(week)
#extend string and number
g=["sunday","monday","tuesday","wenesday","thursday","friday","staturday"]
h=[121,321,231,121,3131,125,121,412,121,1421,112]
g.extend(h)
print(h)
#index passing string as parameter
j=g.index("tuesday")
print(j)
#index number as passing parameter
k=h.index(412)
print(k)
#insert string
a.insert(0,"jan")
print(a)
#pop
b.pop(1)
print(b)
#pop element storing into  variables
o=week.pop(5)
print(o)
#remove a string
w=["siva", "sakthi","yugi","pradeep"]
w.remove("yugi")
print(w)
#reverse
w.reverse()
print(w)
#sort
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
#max value
t=max(h)
print(t)
#length
u=len(week)
print(u)
#minimum value
i=min(s)
print(i)
#list(seq)
i="sakthi"
v=list(i)
print(v)
