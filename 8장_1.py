


try:
    a=1/0
except:
    print('안된다고')


while(True):
    try:
        a,b=input('두 수를 입력하시오: ').split(',')      # ',' 앞뒤로 문자열을 분리 
        result=int(a)/int(b)
        print('{}/{}={}'.format(a,b,result))
        break
    except:
        print('다시')


str3=input('세 숫자를 입력:')         #하나의 문자열 
print(str3)


str3=input('세 숫자를 입력:').split(',')     #문자열 분리
istr3=map(int,str3)                          #각 문자열별 int 
print(str3)


a,b,c=map(int,input('세 숫자를 입력:').split(','))     
print(a,b,c)



