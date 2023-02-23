s="sssaassaaall"
l=list(s)
string=""
i=0
while i<len(s):
    count=0
    j=0
    while j<len(l):
        if s[i]==l[j]:
            count+=1
        else:
            #j=len(l)-1
            break
        j+=1
    string+=s[i]+str(count)
    i+=count
    for k in range(count):
        l.pop(0)
print(string)
