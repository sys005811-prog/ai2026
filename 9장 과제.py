
#9-1
print((200).__sub__(100)) #100
print((200).__mul__(100)) #20000
print((200).__truediv__(100)) #2.0
 
print([10,20,30,40].pop()) #40

 # keys, get은 딕셔너리 

print(dir(int))
print(dir(list))


#9-2

#객체 지향 프로그래밍: 수행 작업을 객체 사이의 상호작용으로 표현
#절차적 프로그래밍: 사전에 생성한 함수나 모듈을 호출하여 작업 수행 
#그래픽 사용자 인터페이스: 시각적 요소 

#객체지향, 절차적 프로그래밍 간 차이점: 유지보수 비용이 객체 지향 프로그래밍이 더 낮음 -> 절차적 프로그래밍에 비해 선호도 높음


#9-3

#클래스: 프로그램상 속성, 행위의 집합체(설계도)
#객체: 클래스로부터 생성된 모든 항목 
#인스턴스: 클래스로부터 생성된 개별적 객체
#클래스 속성: 객체의 상태
#클래스 동작: 객체의 기능


#9-4
class Dog:
    def bark(self):
        print('멍멍~~')

my_dog=Dog()
my_dog.bark()

#9-5
class Dog:
    def bark(self):
        print('멍멍~~')

    def __init__(self,name):
        self.name=name

my_dog=Dog('Jindo')
my_dog.bark()        


#9-6
class Dog:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'my_dog의 정보: Dog(name='+self.name+')'

my_dog=Dog('Jindo')
print(my_dog)


#9-7
n=100
m=100
if n is m:
    print('n is m')
else:
    print('n is not m')
  #n is m
   # n,m의 값이 모두 100으로 같음


#9-8
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)
    def __truediv__(self,other):
        return Vector(self.x/other.x,self.y/other.y)
    def __str__(self):
        return'({},{})'.format(self.x,self.y)
    
v1=Vector(30,40)
v2=Vector(10,20)

v3=v1*v2
v4=v1/v2

print('v1*v2=',v3)
print('v1/v2=',v4)

class Vector1:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __neg__(self):
        return(-self.x,-self.y)
    def __str__(self):
        return'({},{})'.format(self.x,self.y)

v1=Vector1(10,20)
v5=-v1
print('-v1=',v5)


#9-9

class Vector2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __gt__(self,other):
        return((self.x**2+self.y**2)**0.5>(other.x**2+other.y**2)**0.5)
    def __ge__(self,other):
        return((self.x**2+self.y**2)**0.5>=(other.x**2+other.y**2)**0.5)
    def __lt__(self,other):
        return((self.x**2+self.y**2)**0.5<(other.x**2+other.y**2)**0.5)
    def __le__(self,other):
        return((self.x**2+self.y**2)**0.5<=(other.x**2+other.y**2)**0.5)
    def __str__(self):
        return'({},{})'.format(self.x,self.y)

v1=Vector2(30,40)
v2=Vector2(10,20)

print('v1>v2=',v1>v2)
print('v1>=v2=',v1>=v2)
print('v1<v2=',v1<v2)
print('v1<=v2=',v1<=v2)


#9-10

class Rect:
    def __init__(self,width,height):
        self.width=width
        self.height=height

r1=Rect(100,200)
print(r1.__dict__)  #{'width': 100, 'height': 200}
print(r1.__dict__['width'])  #100


class Rect:
    def __init__(self,width,height):
        self.__width=width
        self.__height=height

r1=Rect(100,200)
print(r1.__dict__) # {'_Rect__width': 100, '_Rect__height': 200}
print(r1.__dict__['_Rect__width']) # 100






























    
