
a = ["sunday","monday","tuesday","wenesday",]
for x in a:
  print(x)

g=["thursday","friday","staturday"]
for i in range(len(g)):
  print(g[i])


b=['jan','feb','mar']
i = 1
while i < len(b):
  print(b[i])
  i = i + 1

[print(x) for x in b]

dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in dict:
  print(x)

c={"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"} 
for x in c:
  print(c[x])

h = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(len(h))

print(h)

print(type(h))

u =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in u.values():
  print(x)


i =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


for x, y in i.items():
  print(x, y)