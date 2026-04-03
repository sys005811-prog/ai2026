


i = 0       # 초기 값
while i < 5:
    print('Welcome to everyone!!')
    i += 1           # i= 1,2,3...    i<5 를 만족하는 한 계속 반복




for i in range(5):
    print('Welcome to everyone!!')   # 위의 while문과 같은 기능

isum=0
i=0
n_list=[0,2,5,10]
while i<len(n_list):     # len(length): 범위, 리스트 항목 수만큼 반복
    isum += n_list[i]     #리스트 내부 i
    i += 1
print(isum)

