

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

