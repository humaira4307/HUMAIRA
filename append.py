a=()
b=()
n1=int(input('enter a size'))
for i in range(0,n1):
    ele=int(input('enter the elements'))
    a.append(ele)
n2=int(input('enter b size'))
for i in range(0,n2):
    ele=int(input('enter the elements'))
    b.append(ele)
for i in a:
    if i in b:
        print(i)