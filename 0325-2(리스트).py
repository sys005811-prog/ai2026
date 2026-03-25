'''
#리스트 함수는 0번째부터 시작 
score=(87, 84, 95, 67, 88, 94, 63)
name =('김','박','이')
print(score)
print(type(score))

for i in score:
    print(i)

for i in name:
    print(i)

for J in score:  #i,J는 모두 변수 이름, 변수 이름을 바꿔도 같은 함수임
    print(J)
'''
'''
score=(87, 84, 95, 67, 88, 94, 63)
name =('김','박','이',score)
add=(('김XX',24,'사람아님'),('박XX',27, '개백수'),('이XX',21,'원숭이'))

for i in add:
    print(i)

ri=list(range(5))   # ri: list 변수화
print(ri)
'''
'''
myString='엄준식'

for ch in myString: #한 글자씩 출력 
    print(ch)
    
listString=list(myString) #리스트화 
print(listString)
'''
'''
a_list=['a', 'b','c', 'd', 'e']
print(a_list[-3])     #리스트의 음수 입력값 -> 뒤쪽부터 출력

a_list.append('f')    #리스트에 'f' 항목 추가
print(a_list)
del a_list[4]         #리스트의 4번째 항목 삭제 
print(a_list)

a_list.remove('a')    #리스트의 'a' 항목 삭제
print(a_list)
'''
'''

a_list=['a', 'b','c', 'd', 'e']    #pop: 맨 뒤 항목을 output으로 지정 후 삭제 
x=a_list.pop()

print(x)
print(a_list)
'''
'''
a_list=[10,20,30,40] #'in'연산으로 리스트 내 항목 존재여부 확인 
print(10 in a_list) 
print(10 not in a_list)


list1= [20, 10, 40, 50, 30]  #sort: 정렬(list1을 정렬된 리스트로 변환)
list1.sort()
print(list1)

list_a= [20, 10, 40, 50, 30] #list_a를 변환하지 않고 정렬된 리스트인 list_b를 생성 
list_b=sorted(list_a)
print(list_a)
print(list_b)
'''

list1=[1,2,3]
list2=[5,6,7,1]

print(list1+list2)     #리스트 합치기


list3=[1,2,3,4]
list4=[4,1,4]
print(list3<list4)     #리스트 크기 비교(첫 항목부터 하나의 항목씩 비교함{사실 잘 모름})






