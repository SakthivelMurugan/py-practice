# l=list("abcdefghijklmnpqrstuvwxyz")
# array=[]
# for i in range(len(l)):
#     if i%2==0:
#         array.append(l[i])
# print(array)

# array2=[l[i] for i in range(len(l)) if i%2==0]
# print(array2)
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[11,12,13,14,15,16,17,18,19,20]
# array=[]
# for i in range(len(l1)):
#     array.append(l1[i]+l2[i])
# print(array)

# array2=[l1[i]+l2[i] for i in range(len(l1))]
# print(array2)

l1=[1,2,3,4,5,6,7,8,9,10]
l2=[11,12,13,14,15,16,17,18,19,20]
array=[]
for i in range(len(l1)):
    if l1[i]%2!=0:
        array.append(l1[i]+l2[i])
print(array)

array2=[l1[i]+l2[i] for i in range(len(l1)) if l1[i]%2!=0]
print(array2)
