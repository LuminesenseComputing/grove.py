'''Class for motion sensors

Status: in progress
Created By: Bipasha Goyal
Last modified: 7 September 2020'''

import time
from grove_mini_pir_motion_sensor import *

class PIR:
    def __init__(self,pin0,pin1):
        self.motion0 = GroveMiniPIRMotionSensor(pin0)
        self.motion1 = GroveMiniPIRMotionSensor(pin1)
        #self.motion2 = GroveMiniPIRMotionSensor(pin2)
    
    def getReadings(self):

        def callback():
            return True
        
        start_time = time.time()
        seconds = 4

        while True:
            elapsed_time = time.time() - start_time

            if elapsed_time < seconds:
                #self.motion0.on_detect = callback
                #self.motion1.on_detect = callback
                #self.motion2.on_detect = callback
                if self.motion0.on_detect or self.motion1.on_detect: #or self.motion2.on_detect:
                    print('Motion detected')
                    return True
            if elapsed_time >= seconds:
                print('No motion')
                return False

pir = PIR(5,16)
pir.getReadings()
