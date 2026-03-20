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
    print("정가요")
'''
'''
time =int(input("몇시냐?"))

    
if time<12:                      # 들여쓰기 꼭 하십쇼 특히 조건문은
    print("오전")
elif time<24:
    print("오후")
else:
    print("하루 시간은 24시까진데요")

'''
'''
num= int(input("정수를 입력하세요:"))
if num % 3 ==0:
    print(num, "은(는) 3의 배수입니다.")
else:
    print(num, '은(는) 3의 배수가 아닙니다.')
