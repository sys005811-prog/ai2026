
'''
class Line:
    length=0
    def __init__(self,length):
        self.length=length
        print(self.length,'길이의 선이 생성됨')

    def __del__(self):
        print(self.length,'길이의 선이 삭제됨')

    def __repr__(self):
        return'선의 길이:'+str(self.length)

    def __add__(self,other):
        return Line(self.length+other.length)

    def __lt__(self,other):
        return self.length<other.length

    def __eq__(self,other):
        return self.length==other.length



Line1=Line(100)
Line2=Line(200)
Line3=Line1+Line2
Line3=Line1+Line2

print(Line1,Line2)

print('두 선 길이의 합:', Line1+Line2)

if Line1<Line2:
    print('Line2가 더 길다.')
elif Line1==Line2:
    print('두 선 길이가 같다.')
else:
    print('몰라레후')

    
print(type(Line3))

del(Line1)
print(Line3)


'''


'''
import time

class Racingcar:
    carname=""
    def __init__(self,name) :
        self.carName=name

    def runCar(self):
        for i in range(0,3):
            carStr=self.carName + '~~달립니다.\n'
            print(carStr,end='')
            time.sleep(0.1)

car1=Racingcar('@자동차1')
car2=Racingcar('!자동차2')
car3=Racingcar('$자동차3')


car1.runCar()
car2.runCar()
car3.runCar()

'''
'''
import threading
import time

class Racingcar:
    carname=""
    def __init__(self,name) :
        self.carName=name

    def runCar(self):
        for i in range(0,3):
            carStr=self.carName + '~~달립니다.\n'
            print(carStr,end='')
            time.sleep(0.1)

car1=Racingcar('@자동차1')
car2=Racingcar('!자동차2')
car3=Racingcar('$자동차3')

th1=threading.Thread(target=car1.runCar)
th2=threading.Thread(target=car2.runCar)
th3=threading.Thread(target=car3.runCar)

th1.start()
th2.start()
th3.start()
'''

import multiprocessing
import time

class Racingcar:
    carname=""
    def __init__(self,name) :
        self.carName=name

    def runCar(self):
        for i in range(0,3):
            carStr=self.carName + '~~달립니다.\n'
            print(carStr, end='')
            time.sleep(0.1)

if __name__=="__main__":
    
    car1=Racingcar('@자동차1')
    car2=Racingcar('!자동차2')
    car3=Racingcar('$자동차3')

    mp1=multiprocessing.Process(target=car1.runCar)
    mp2=multiprocessing.Process(target=car2.runCar)
    mp3=multiprocessing.Process(target=car3.runCar)
      
    mp1.start()
    mp2.start() 
    mp3.start()

    mp1.join()
    mp2.join()
    mp3.join()

'''
import time

class RacingCar :
    carName = ''
    def __init__(self, name) :
        self.carName = name

    def runCar(self) :
        for _ in range(0,3) :
            carStr = self.carName + '~~ 달립니다.\n'
            print(carStr, end = '')
            time.sleep(0.1)

car1 = RacingCar('자동차1')
car2 = RacingCar('자동차2')
car3 = RacingCar('자동차3')

car1.runCar()
car2.runCar()
car3.runCar()

import multiprocessing
import time

if __name__ == "__main__" :
    car1 = RacingCar('자동차1')
    car2 = RacingCar('자동차2')
    car3 = RacingCar('자동차3')

    mp1 = multiprocessing.Process(target = car1.runCar)
    mp2 = multiprocessing.Process(target = car2.runCar)
    mp3 = multiprocessing.Process(target = car3.runCar)

    mp1.start()
    mp2.start()
    mp3.start()

    mp1.join()
    mp2.join()
    mp3.join()

'''

