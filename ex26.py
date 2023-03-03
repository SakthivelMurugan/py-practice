l=[]
n=int(input("enter limit :"))
for i in range(n+1):
    l.append(i)
array=[]
for i in range(1,int(len(l)/2)):
    array2=[]
    if len(l)>=i:
        for j in range(i):
            array2.append(l[j])
        array.append(array2)
        for z in range(len(array2)):
            l.remove(array2[z])
    else:
        break
print(array)