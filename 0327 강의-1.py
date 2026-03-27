
# end: 끝,() 안에 기호 삽입, 내용 없을시 \(줄바꿈) 자동 삽입
'''
for i in range(5):

    print(i, end = ' ')   #줄바꿈x

    print(i, end = '\n')  #줄바꿈x

    print(i)


for i in range(-2, -10, -2):
    print(i, end = ' ')
'''
    

s=0                         #변수 초기화 
for i in range (1,11):
    s= s+i
print('1에서 10까지의 합:', s)



s=0
for i in range (1,11):
    s= s+i
    print('i={}, s={}'.format(i,s))
print('1에서 10까지의 합:',s)


n=int(input('수 입력:'))
s=0
for i in range(0,n):
    s=s+(i+1)
print('1부터 {}까지의 합은 {}'.format(n,s))
print('1부터',n,'까지의 합은',s)
