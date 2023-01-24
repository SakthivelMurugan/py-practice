a=[1,2,3,4,6]
b=[2,1,3,13,8,10,6,7]

#intersection
for i in b:
    if i not in a:
        a.append(i)
b=sorted(a)
print(b)
z=b[-1]
y=[]
for i in range(z):
    if i not in b:
        y.append(i)
print(y)


#union
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print("union",sorted(c))




