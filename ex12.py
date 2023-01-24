string="sak2thi h4i ve3l m1r"

string1=""
ar=[]
for i in string:
    if i!=" ":
        string1+=i
    else:
        ar.append(string1)
        string1=""
ar.append(string1)
n=[]
c=[]
for i in ar:
    s=""
    for j in i:
        if j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            n.append(int(j))
        else:
            s+=j
    c.append(s)
i=0
l=len(n)
ss=""
while i<l:
    ss+=c[n.index(min(n))]+" "
    c.pop(n.index(min(n)))
    n.remove(min(n))
    i+=1
print(ss)



