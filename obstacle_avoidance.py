import RPi.GPIO as GPIO
import time
  
from distance import CarUltrasound
import robot

import os


GPIO.setwarnings(False)  # Disable warning
GPIO.setmode(GPIO.BCM)  # BCM coding 



def start():
    try:
        start_time = None

        while True:
            move_status_file = '/home/pi/Workspace/move_status/forward_status'
            flag=os.path.exists(move_status_file)
            print(flag)
            if (flag == False):
                robot.stopFB()
                robot.stopLR()
                GPIO.cleanup()
                break
                    # perception
            car = CarUltrasound()
            dist_mov_ave = car.DistMeasureMovingAverage()
            print('Distance', dist_mov_ave)

                    # decison-making
            if (start_time is None) or (time.time() - start_time >  0.5):
                start_time = None
                if dist_mov_ave < 20:
                    print("Going left")
                    robot.stopFB()        
                    robot.left()
                    time.sleep(2)
                    robot.stopLR()
                    robot.forward()
                    start_time = time.time()
                elif dist_mov_ave < 100:
                    print("Going Forwaed " + str(dist_mov_ave/2 + 40))
                    robot.forward()
                    time.sleep(1)
                else:
                    print("Going Forwaed 90")
                    robot.forward(1)
                    time.sleep(3)
            else:
                pass

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        
if __name__ == '__main__':
    start()
