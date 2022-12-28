'''#1
a=int(input("enter number 1"))
b=int(input("enter number 2"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

#2 
number=int(input("enter number"))
if number%2==0:
    if number%8==0:
        if number%14==0:
            print("true")
else:
    if number%3==0:
        if number%7==0:
            print("this odd number is number divisible by 3 and 7")
    else:
        if number%11==0:
            print("this odd number is not divisible by 3 and divisible by 11")'''

#3
months=['january','february','march','april','may','june','july','august','september','october','november','december']
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
temp=[]
temp2=[]
for i in range(len(months)):
    for j in range(len(days)):
        temp.append(months[i])
        temp.append(days[j])
        temp2.append([months[i],days[j]])
print(temp)
print(temp2)

'''l=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
ip={"even":[],"odd":[]}
for i in range(len(l)):
    if l[i]%2==0:
        even.append(l[i])
        ip["even"].append(l[i])
    else:
        odd.append(l[i])
        ip["odd"].append(l[i])
op={"even":even,"odd":odd}
print(op)
print(ip)'''



