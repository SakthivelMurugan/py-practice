# n=5
# for i in range(n):
#     j=0
#     while j<n:
#         if i==0 or j>=i:
#             print("*",end="")
#             j+=1
#         else:
#             print(" ",end="")
#             j+=1
#     else:
#         print()

n=5
i=0
a=n-1
while i<n:
    j=0
    while j<n:
        if j==a or j>a:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    else:
        print()
        i+=1
        a-=1