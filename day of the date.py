import math
date=int(input('enter the date:'))
month=int(input('enter the month:'))
year=int(input('enter the year:'))
month=month-2
c=year//100
d=year%100
f=date+((13*month-1)/5)+d+(d//4)+
fres=int(f%7)
day={0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}
print(day[fres])