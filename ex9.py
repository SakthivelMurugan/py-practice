str1=str(input("enter user name :"))
length=int(0)
fc=int(0)
sc=int(0)
num=int(0)
if(len(str1)>=8):
    length=1
if(str1[0]>='A' and str1[0]<='Z'):
    fc=1
for i in range(len(str1)):
    if((str1[i]>='A' and str1[i]<='Z') or (str1[i]>='a' and str1[i]<='z')):
        sc=sc
        num=num
    elif str1[i]=="1" or str1[i]=="2" or str1[i]=="3" or str1[i]=="4" or str1[i]=="5" or str1[i]=="6" or str1[i]=="7" or str1[i]=="8" or str1[i]=="9" or str1[i]=="0":
        num=1
    else:
        sc=1
if(length==1 and fc==1 and sc==1 and num==1):
    print(str1," is valid username")
else:
    print(str1," is not valid username")
