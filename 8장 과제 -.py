

'''
#8-1

a=[10,20,30]

a[3]            #IndexError: list index out of range                            리스트에 없는 항목 

n=int('20%')    #ValueError: invalid literal for int() with base 10: '20%'      숫자가 아닌 항목을 int로 바꿈 

a=100+'200'     #TypeError: unsupported operand type(s) for +: 'int' and 'str'  문자열+숫자


try:
    a[3]
except Exception as e:
    print(e)

try:
    n=int('20%')
except Exception as e:
    print(e)

try:
    a=100+'200' 
except Exception as e:
    print(e)


#8-2

try:
    10*(30/0)
except ZeroDivisionError:
    print('0으로 나눔은 불가능합니다')

try:
    X=int(input('정수 x를 입력하세요:'))         
except:
    print('정수를 입력하세요')
else:
    print(X)

import sys

try:
    f=open('myfile.txt')
    s=f.readline()
except FileNotFoundError:
    print('파일을 찾을 수 없습니다')
'''

#8-3

a=[1,2,3,4,5]
print(a)
try:
    b=int(input('a의 요소를 하나 선택하시오:'))
    index=a.index(b)
    print(b,'은(는)', index+1,'번째 요소입니다.')

except:
    print('오류: 입력값이 정수나 실수가 아님')

