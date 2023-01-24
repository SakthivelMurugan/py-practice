n=2
for i in range(n):
    j=0
    while j<n:
        if i==0 or j>=i:
            print("*",end="")
            j+=1
        else:
            print(" ",end="")
            j+=1
    else:
        print()