import datetime as d
import calendar as c

d1=d.datetime.now()
y=int(input('Enter Your Year : '))
m=int(input('Enter Your Month : '))
d=int(input('Enter Your Day : '))

yy=d1.year-y
mm=d1.month-m
if mm<0:
    yy-=1
    mm+=12
    dd=d1.day-d
    if dd<0:
        mm-=1
        dd+=30
else:
    dd=d1.day-d
    if dd<0:
        mm-=1
        dd+=30
        
print("Your Age is =  ")
print(yy,'years ',mm,'months ',dd,'days')
    
     