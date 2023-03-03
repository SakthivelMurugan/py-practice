array=[1,2,3,4,5,1,2,3,4,5,6]
check=int(input("enter count :"))
l=[]
for i in array:
    count=0
    for j in array:
        if i==j:
            count+=1
    if count==check and i not in l:
        l.append(i)
        print(i)
