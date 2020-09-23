'''
Class for Ultrasonic Sensors

Status: in progress
By: Bipasha Goyal
Last modified: September 7, 2020
'''
import time 
from grove_ultrasonic_ranger import *

class Ultrasonic:
    def __init__(self,pin0,pin1):
        self.dist0 = GroveUltrasonicRanger(pin0)
        self.dist1 = GroveUltrasonicRanger(pin1)
        #self.dist2 = GroveUltrasonicRanger(pin2)

    def getReadings(self):
        '''Function called in Main control function.
        Takes average of readings over a defined time interval. Then averages all readings from all sensors.'''
        start_time = time.time()
        seconds = 4 #can change time here

        dist0_read = []
        dist1_read = []
        #dist2_read = []

        while True:
            elapsed_time = time.time() - start_time

            if elapsed_time < seconds:
                dist0_read.append(self.dist0.get_distance())
                dist1_read.append(self.dist1.get_distance())
                #dist2_read.append(self.dist2.get_distance()) 
            if elapsed_time >= seconds:
                break 
        #print(dist0_read)
        #print(dist1_read)
        
        dist_ave =[sum(dist0_read)/len(dist0_read),sum(dist1_read)/len(dist1_read)]
        dist_final = sum(dist_ave)/len(dist_ave)
        return dist_final
        #return  dist_final = mean([mean(dist0_read),mean(dist1_read),mean(dist2_read)])

sonar = Ultrasonic(5,16)
print('Detecting distance...')
print('{} cm'.format(sonar.getReadings()))
    
