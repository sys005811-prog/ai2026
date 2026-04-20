
#7-1

import datetime
a=datetime.datetime.now()
print('오늘의 날짜:', a.year,'년', a.month, '월', a.day,'일')
if a.hour >=12:
    print('현재시간:', '오후', a.hour,'시' , a.minute, '분', a.second, '초')
else:
    print('현재시간:', '오전', a.hour,'시' , a.minute, '분', a.second, '초')



#7-2

import datetime as dt
today = dt.date.today()
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas- dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
print('2026년 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds // 3600))

new_year=dt.datetime(2036, 1, 1)
time_gap_1 = new_year - dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
print('2036년 새해 까지는 {}일 {}시간 남았습니다.'.format(time_gap_1.days,time_gap_1.seconds // 3600))

birthday=dt.datetime(2026, 5, 3)
time_gap_2 = birthday - dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
print('2026년 생일 까지는 {}일 {}시간 남았습니다.'.format(time_gap_2.days,time_gap_2.seconds // 3600))


#7-3

print('오늘:',dt.date.today())
K=dt.timedelta(days=1000)
plusKday=dt.date.today()+K
print('1000일 후', plusKday)


A,B,C=map(int,input('처음으로 사귄 연도와 월, 일을 입력하시오:').split())

a=dt.date(A,B,C)
b=a+dt.timedelta(days=100)
print('100일 기념일은:', b.year,'년', b.month,'월', b.day,'일')


#7-4

import math as m
for i in range(2,11):
    print('4**',i,'=',4**i)

for d in range(0,181,10):
    print(d,'degree =',m.radians(d),'radian')

for s in range(0,181,10):
    print('sin(',s,') =',m.sin(m.radians(s)))


#7-5

import random as rd

a = []
for i in range(3):
    a.append(rd.randrange(0, 101, 5))
print('0에서 100 이하의 정수 중에서 5의 배수\n', a)

a=list(range(1,11))
b=rd.sample(a,3)
print('1에서 10 사이의 임의의 정수:',b)


#7-7
import turtle as t
 #1,2
for i in range(3):
    t.forward(200)
    t.left(120)
for j in range(3):
    t.forward(100)
    t.left(120)

 #3
import turtle as t
for a in [300,200,100]:
    for b in range(3):
         t.forward(a)
         t.left(120)
            
 #4
import turtle as t

for q in range(4):
    t.forward(100)
    t.left(90)
