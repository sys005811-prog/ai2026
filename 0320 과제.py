# 3-1
game_score=int(input('game_score:'))
print('game_score', game_score)
if game_score >=1000:
    print('당신은 고수입니다')
'''
'''
num_a=int(input('숫자 a를 입력하세요:'))
num_b=int(input('숫자 b를 입력하세요:'))
print('num_a:',num_a)
print('num_b:', num_b)
if num_a == num_b:
    print('두 값이 일치합니다.')

'''
'''
# 3-2
n=int(input('1~100 사이 정수 n을 입력하세요:'))
if n>100 or n<0:
    print('1~100 사이 정수를 입력하세요')

elif n % 2 == 0:
    print('n =', n )
    print("n 은(는) 짝수입니다")
else:
    print('n =', n)
'''
'''
x=int(input('-100~100 사이 정수 x를  입력하세요:'))
if x>100 or x<-100:
    print('-100~100 사이 정수를  입력하세요')
elif x>0:
      print('x =',x)
      print('x 은(는) 자연수입니다')
else:
    print('x =', x)
'''
'''
# 3-3
game_score=int(input('게임점수를 입력하시오:'))
if game_score >= 1000:
    print('game_score:',game_score)
    print('고수입니다')
else:
    print('game_score:',game_score)
    print('입문자입니다')
'''
'''
n_a=int(input('한 정수를 입력하시오:'))
n_b=int(input('다른 정수를 입력하시오:'))
if n_a==n_b:
    print('두 값이 일치합니다')
else:
    print('두 값이 일치하지 않습니다')
'''
'''
n=int(input('당신은 성인인가요(성인이면 1, 미성년이면 0):'))
if n==0:
    print('당신은 미성년자입니다')
else:
    a=int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0):'))
    if a==1:
        print('당신은 결혼한 성인입니다')
    else:
        print('당신은 결혼하지 않은 성인입니다')
'''
'''
# 3-4
num=int(input('num:'))
if num>=1 and num<=10:
    print('True')
'''
'''
age=int(input('age:'))
if age>10 and age<19:
    print('청소년입니다')
'''
'''
# 3-5
speed=int(input('자동차의 속력을 입력하세요(단위: km/h):'))
if speed >=100:
    print('고속')
elif speed<100 and speed>=60:
    print('중속')
else:
    print('저속')
