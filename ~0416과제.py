'''

#6-1

capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}

print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])


#6-2

person = {'이름':'홍길동', '나이':26, '몸무게':82}
person['특기'] = '분신술'
person['아버지'] = '홍판서'
print(person)

del person['나이']
print(person)


#6-3

capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}

print('Korea' in capital_dic)       #true
print('China' in capital_dic)       #true
print('Indonesia' in capital_dic)   #false
print('Beijing' in capital_dic)     #false


#6-4

fruits_dic = {'apple':6000, 'melon':3000, 'banana': 5000, 'orange':7000}
print(fruits_dic.keys())
print(fruits_dic.values())
fruits_dic.pop('apple')
print(fruits_dic)
fruits_dic.clear()
print(fruits_dic)


#6-5

fruits_dic = {'apple':6000, 'melon':3000,'banana': 5000, 'orange':4000}
print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))
print(len(fruits_dic))


a=input('키 입력:')
if a in fruits_dic:
    print(a, 'is in fruits_dic.')
else:
    print(a, 'is not in fruits_dic.')

'''
#6-6

the_day= (1919, 3, 1)
print(the_day[0],'년', the_day[1],'월', the_day[2], '일은 삼일절입니다')


list_a=[10,20,30]
tup_a=tuple(list_a)
c,b,a=tup_a
print('a=',a)
print('b=',b)
print('c=',c)


#6-7

person=('홍길동', 2019001, 179)
print('person=',person)
'''
person[1]=2019003           #오류: 튜플 내 항목 수정 불가
'''
list_a=list(person)
list_a[1]=2019003
person=tuple(list_a)
print('학번 변동 후 person =', person)


#6-8

def square(x, y):
    x_sq= x**2
    y_sq= y**2
    return x_sq,y_sq
x=10
y=20
x_sq, y_sq= square(x,y)
print('{}제곱={},{}제곱={}'.format(x,x_sq,y,y_sq))

a=(10,20,30)+(40,60,60)
print(a)


print('Hello'*3)            #문자열의 반복
print(('Hello',)*3)         #튜플의 반복
a='Hello'
b=('Hello',)
print(type(a))              
print(type(b))


#6-9

lst=['apple','mango','banana']
s1=set(lst)
print(s1)

greet='Good afternoon'
s2=set(greet)
print(s2)


#6-10

s1={10,20,30,40}
s2={30,40,50,60,70}
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))

#6-11

A={1,2}
B={'A','B','C'}

def product_set(set1,set2):
    result=set()
    for i in set1:
        for j in set2:
            result=result|{(i,j)}
    return result

A={1,2}
B={'A','B','C'}

AxB=product_set(A,B)
print('AxB=',AxB)

BxA=product_set(B,A)
print('BxA=',BxA)

AxA=product_set(A,A)
print('AxA=',AxA)

BxB=product_set(B,B)
print('BxB=',BxB)


















