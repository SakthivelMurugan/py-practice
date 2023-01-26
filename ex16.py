string="@!sakthi%$vel@siva"
word=[]
for i in string:
    if(i>="a" and i<="z")or(i>="A" and i<="Z"):
        word.append(i)
    else:
        word.append("|")
push=""
ar=[]
for i in word:
    if i!="|":
        push+=i
    else:
        ar.append(push)
        push=""
ar.append(push)
br=[]
temp=[]
for i in ar:
    if i!="":
        x=len(i)-1
        while x>=0:
            temp.append(i[x])
            x-=1

op=""
for i in string:
    if(i>="a" and i<="z")or(i>="A" and i<="Z"):
        op+=temp[0]
        temp.pop(0)
    else:
        op+=i
print(op)

            

