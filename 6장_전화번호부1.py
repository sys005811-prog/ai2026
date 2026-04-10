#전화번호부

import json  #import:모듈 불러오기 


#주소록
adressbook={
    'AC':'010-1234-4321',
    'DC':'010-3213-6721'
}

#파일로 저장

with open('adressbook.json','w',encoding='utf-8') as f:
    json.dump(adressbook,f,ensure_ascii=False,indent=4)          #json에 adressbook을 함수 형태 저장 

print('주소록이 저장되었습니다.')



#파일에서 다시 불러오기

with open ('adressbook.json','r',encoding='utf-8') as f:
    adressbook=json.load(f)

print('불러온 주소록:',adressbook)
print('AC 번호:',adressbook['AC'])

