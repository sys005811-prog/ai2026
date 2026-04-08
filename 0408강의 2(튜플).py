


# 리스트 변수: 대괄호, 변경 가능
# 튜플 변수: 소괄호, 변경 불가

'''
tuple1=(1,2,3,4)
tuple1[0]=1            #재지정 불가 -> 에러 뜸 

print(tuple1[0])
'''

def plusminus(a1,a2):
    return a1+a2, a1-a2

output=plusminus(10,2)
print(type(output))         # 함수는 튜플 형식 -> 수정불가 

output_list=list(output)    # output을 리스트 변수로 변경
print(output_list)



a=(1,2)   #패킹
print(a[0])

b=(5,6)
c,d=b     #언패킹 
print(c)  




a=100
b=200

print('Before swap: ', a,b)

a,b = b,a                   # 스왑(패킹,언패킹)

'''
a=b                         # a값이 b값으로 변경 (200,200)
b=a                         # 그대로 200,200
'''

print('After swap: ', a,b)




tuple2=(1,6,2,3,4,5)
print(tuple2.count(2))     #  count(x): x의 수
print(tuple2.index(1))     #  index(x): x의 위치 


