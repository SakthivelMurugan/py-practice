n=153
num=n
i=0
while(n>0):
    n=(n-(n%10))/10
    i+=1
ans=0
while(num>0):
    rem=num%10
    ans+=rem**i
    num=(num-(num%10))/10
    i-=1
print(int(ans))
