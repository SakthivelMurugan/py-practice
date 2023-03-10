string="sakt1hi h0i how2 yo4u ar3e"
temp=""
dic={}
for i in range(len(string)):
    if (string[i]>='a' and  string[i]<='z') or (string[i]>='A' and  string[i]<='Z'):
        temp+=string[i]
        if i==len(string)-1:
            dic[temp2]=temp
    elif string[i] in list("0123456789"):
        temp2=int(string[i])
        if i==len(string)-1:
            dic[temp2]=temp
    elif string[i]==" ":
        dic[temp2]=temp
        temp=""
result=""
for j in sorted(dic):
    result+=dic[j]+" "
print(result)

