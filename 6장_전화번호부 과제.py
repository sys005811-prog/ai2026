#전화번호부

import json  


#저장된 주소록 불러오기

with open('adressbook.json', 'r', encoding='utf-8') as f:
    adressbook = json.load(f)

#주소록에 항목  추가
                           
name=None

while(True):
    name=input('이름을 입력하세요:')
    if(name == '끝'):
        break
    else:
        phonenumber=input('전화번호를 입력하세요:')
        adressbook[name]=phonenumber

while(True):
    name=input('삭제할 이름을 입력하세요:')
    if(name == '끝'):
        break
    else:
        del adressbook[name]

#파일로 저장

with open('adressbook.json','w',encoding='utf-8') as f:
    json.dump(adressbook,f,ensure_ascii=False,indent=4)          

print('주소록이 저장되었습니다.')

print('불러온 주소록:',adressbook)



