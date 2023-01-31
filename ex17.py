# dic={1:"sakthi",2:"vel"}
# dic.update({3:"M"})
# print(dic)


a="sakthivel"
a=list(a)
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
s=""
for i in a:
    s+=i
print(s)
