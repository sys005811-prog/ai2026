


import datetime                  #현재 시간 
print(datetime.datetime.now())

today=datetime.date.today()
print(today.day)

now=datetime.datetime.now()
print(now.month)


dir(datetime)         #dir(): ()안의 모듈의 모든 클래스 목록 출력
print(dir(datetime))


import datetime as dt  # import A as B: A모듈명을 B로 바꿈(주로 단순하게 줄임)
print(dt.datetime.now()) # 두 번째 datetime은 모듈명이 아닌 클래스명

