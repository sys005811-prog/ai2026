'''
class Rectangle:
    def __init__(self, side=0):
        self.side = side
    def getArea(self):
        return self.side*self.side

r1=Rectangle(10)


def printAreas(r, n):
    while n >= 1:
        print(r.side, "\t", r.getArea())
        r.side = r.side + 1
        n = n - 1




class Television:
    serialNumber = 0
    def __init__(self):
        Television.serialNumber += 1
        self.number = Television.serialNumber
    def __str__(self):
        return '{}'.format(self.number)



t1=Television()
t2=Television()
myTv=Television()

print(t1,t2)
'''


class Car:
    

    def __init__(self,name="",speed=0):   #기본값 지정 필수 
        self.name=name
        self.speed=speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def __str__(self):
        return '{}의 속도는,{}km/h'.format(self.name,self.speed)

    def speedUp(self,value):
        self.speed += value
       
    def speedDown(self,value):
        self.speed -= value
    

class Sedan(Car):
    def speedUp(self, value):
        self.speed +=value
        if self.speed >150:
            self.speed =150

    def speedDown(self, value):
        self.speed -=value
        if self.speed <0:
            self.speed =0
myCar=Sedan("k5",20)
myCar.speedUp(2250)
print(myCar)



















