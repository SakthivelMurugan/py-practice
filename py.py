# str1=["s","a","k","t","h","i"]
# str2=["s","i","v","a"]
# for i in range(0,len(str1),1):
#     for j in range(0,len(str2),1):
#         if str1[i]==str2[j]:
#             str1.remove(str1[i])
#             str2.remove(str2[j])
#             j-=1          



str1=str(input("enter name1 :"))
str2=str(input("enter name2 :"))
l=[]
for i in str1:
    l.append(i)
str1=l

l=[]
for i in str2:
    l.append(i)
str2=l
i=0
while i<len(str1):
    j=0
    while j<len(str2):
        if str1[i]==str2[j]:
            str1.pop(i)
            str2.pop(j)
            j=len(str2)-1
            i=i-1
        j+=1
    i+=1
string=str1+str2
l=len(string)
array=["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
length=len(array)-1
i=0 
k=0
while i<length:
    j=0
    while j<l:
        if k==len(array):
            k=0
        if j==l-1:
            array.pop(k)
            k-=1
        j+=1
        k+=1
    i+=1
print(array)





