def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def is_leap_year(year):
    if(year%4==0 and year%100!=0)or(year%400==0):
        return True
    else:
        return False
inputs=[]
for i in range(5):
    num=int(input("enter a number:"))
    inputs.append(num)

for num in inputs:
    if is_prime(num):
        print(num,"is a prime number")
    if is_leap_year(num):
        print(num,"is a leap year:")
        

    
    
    


