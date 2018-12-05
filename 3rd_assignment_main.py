#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time

 
class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.dislist = [50, 50] 

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        counter = 0 
        while 1:
            distanceSensor = self.car.distance_detector
            if distanceSensor.get_distance() > 2:
                distance = distanceSensor.get_distance()
                self.dislist[0] = self.dislist[1]
                #self.dislist[1] = self.dislist[2]
                self.dislist[1] = distance
            avdistance = (self.dislist[1] + self.dislist[0])//2
            
            self.car.accelerator.go_forward(100)
            deftracker = self.car.line_detector
            tracker = deftracker.read_digital()
            if tracker == [1, 1, 0, 0, 0]:
                self.car.steering.turn(105)
                time.sleep(0.0001)
            elif tracker == [1, 0, 0, 0, 0]:
                self.car.steering.turn(97)
                time.sleep(0.0001)
            elif tracker == [0, 1, 0, 0, 0]:
                self.car.steering.turn(115)
                time.sleep(0.0001)
            elif tracker == [0, 0, 0, 1, 0]:
                 self.car.steering.turn(65)
                 time.sleep(0.0001)
            elif tracker == [0, 0, 0, 1, 1]:
                 self.car.steering.turn(75)
                 time.sleep(0.0001)
            elif tracker == [0, 0, 0, 0, 1]:
                 self.car.steering.turn(83)
                 time.sleep(0.0001)
            elif tracker == [1, 1, 1, 1, 1] and counter  < 4:
                 self.car.steering.turn(65)
                 time.sleep(0.0001)
            #elif tracker == [0, 0, 0, 0, 0]:
            #    print(tracker)
            #    self.car.steering.turn(125)
            #    self.car.accelerator.go_backward(45)
            #    time.sleep(0.05)
            #    newtracker = deftracker.read_digital()
            
            
            #if avdistance <=25:
            #    self.car.steering.turn(67)
            #    time.sleep(0.4)
            ##    self.car.steering.turn(90)
             #   time.sleep(0.4)
             #   self.car.steering.turn(125)
             #   counter += 1
             #   print(counter)
             #   
             #   time.sleep(0.6)
             #   self.car.steering.turn(90)
             #   time.sleep(0.2)
            else:
                pass 
                
            if counter >= 4 and tracker == [1, 1, 1, 1, 1]:
                myCar.drive_parking()
                break
                



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()