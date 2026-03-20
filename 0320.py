num=0
for i in range(3):
    num +=100   #num += 100 -> num = num + 100
    print('num=', num)
'''
'''
num=0
for i in range(11):
    num +=100
    print('1th num=', i, num)
'''
'''
age =int(input("나이를 입력하세요:"))   #input:입력 상태로 대기 #int;문자열 변환
if age< 20:
    print("청소년 할인")            #if:첫 조건, elif: 앞 조건이 아닐때 추가 else: 맨마지막 조건(단 1개만)
elif age >=65:
    print("지게에 타라 할배")
else:
    print("돈내놔라")

