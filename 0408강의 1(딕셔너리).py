

#딕셔너리 : 키,값으로 구성 
# 키: 이름, 나이, 몸무게         값: 홍길동, 24, 150

person={'이름': '홍길동', '나이':24 , '몸무게': 150}


person['국적']='대한민국'     #새로운 항목 삽입 
print(person)                 #수정된 딕셔너리 출력 

del person['나이']            #기존 항목 삭제 

print(person['국적'])
print(person['이름'])
print(person['몸무게'])

print(person.keys())          # keys(): 딕셔너리 내 키 반환 

print(person.values())        # values(): 값 반환


for key in person:                          # for 루프 이용 
    print('{}:{}'.format(key,person[key]))











