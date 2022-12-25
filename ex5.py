def superReducedString(s):
    s=s.lower()
    ar=[]
    for i in range(len(s)):
        ar.append(s[i])
    ar2=[]
    for j in range(len(ar)):
        if ar[j] not in ar2:
            ar2.append(ar[j])
    a=[]
    for i in range(len(ar2)):
        count=0
        for j in range(len(ar)):
            if ar2[i]==ar[j]:
                count=count+1
        if count%2!=0:
            a.append(ar2[i])
    str=""
    for z in range(len(a)):
        str+=a[z]
    if str=="":
        return "Empty String"
    else:
        return str

print(superReducedString("abbaabbb"))

