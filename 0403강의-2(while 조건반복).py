



# 지정된 입력값 이외의 값 입력시, 반복 
selected = None                                                # 0으로도 초기화 가능, 문자열이라 Npne으로 초기화 
while selected not in ['가위', '바위', '보']:                   #리스트의 항목에 있는 값 입력시: False(반복 실행 X)
                                                                #없는 경우 True(반복 실행)
    selected = input('가위, 바위, 보 중에서 선택하세요> ')
print('선택한 값은:', selected)





