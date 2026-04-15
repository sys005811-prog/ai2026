




import math as m
print(m.pow(2,3))

print(m.sin(m.pi/2))


import random as R
print(R.random())      #0~1사이 무작위 실수 생성

a=list(range(1,11))
print(a)

R.shuffle(a)           #리스트 항목 셔플 
print(a)


'''
import turtle as t
t.setup(width=500,height=500)
for i in range(250):
    t.forward(i)      #i만큼 전진
    t.left(80)        #왼쪽으로 ()도 회전
t.done()
'''
