def fun(ar):
    ar2=[]
    for i in ar:
        if i not in ar2:
            ar2.append(i)
    i=0
    while i<len(ar2):
        j=0
        while ar2[i]<=ar2[j]:
            if j==len(ar2)-1:
                ar2.remove(ar2[i])
                break
            j+=1
        i+=1

    i=0
    while i<len(ar2):
        j=0
        while ar2[i]<=ar2[j]:
            if j==len(ar2)-1:
                print(ar2[i])
                break
            j+=1
        i+=1
        
fun([0,1,2,3,4,5])