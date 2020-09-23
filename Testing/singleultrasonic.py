from grove_ultrasonic_ranger import *
import time 
from statistics import mean

class singleultrasonic():
    def __init__(self):
        self.dist0 = GroveUltrasonicRanger(pin0)
