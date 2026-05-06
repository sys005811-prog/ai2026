'''
student1={'name':'민수','score':85}    #딕셔너리 
student2={'name':'지영','score':92}


def get_grade(student):               #딕셔너리 변수 함수
    if student['score']>=90:
        return 'A'
    elif student['score']>=80:
        return 'B'
    else:
        return 'C'
print(get_grade(student1))
print(get_grade(student2))
'''


class student:

    def __init__ (self,name,score):                        #init함수 선언(class 초기화 
        self.name=name
        self.score=score

    def __str__(self):
        return'이름:{}, 점수: {}'.format(self.name,self.score)
'''  
    def get_grade(self):               
        if self.score >=90:
            return 'A'
        elif self.score >=80:
            return 'B'
'''

민수=student('민수',85)          #민수=self  student=클래스 생성(괄호 안 항목 2개=함수 input2개)
                                #민수.name=name   민수.score=score
지영=student('지영',92)
'''
print(민수.get_grade())
print(지영.get_grade())   
'''
print(민수)
print(민수.name)                #캡슐화: 객체 이름에 __삽입        ex) self.__name         객체 정보 보
print(민수.score)

        
class phone:
    def __init__(self,brand,battery):
        self.brand=brand
        self.battery=battery
        
    def use(self,minutes):
        self.battery -= 0.5*minutes
        print(self.battery,'%')
    def charge(self,minutes):
        self.battery += minutes
        print(self.battery,'%') 
    
    
my_phone=phone('galaxy',80)

my_phone.charge(20)
my_phone.use(30)


print(my_phone.brand,my_phone.battery,'%')
