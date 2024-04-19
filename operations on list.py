a=(10,20,30,40,50)
b=(60,70,80,90,100)
c=a+b
print(c)
print(type(a))
print(c*2)
print(a*2)
print(b*2)
print(len(c))
print(max(c))
print(min(c))
print(sum(c))
for i in a:
    if i in b:
        b.append(i)
print(b)