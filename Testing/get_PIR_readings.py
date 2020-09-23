import sys
import time 
# insert at 1, 0 is the script path (or '' in REPL)
# Import path to library folder
#sys.path.insert(1,'../grove/')

from grove_mini_pir_motion_sensor import *

def main():
    # change pin number here
    pin1 = 5
    pin2 = 16
    #start_time = time.time()

    pir1 = GroveMiniPIRMotionSensor(pin1)
    pir2 = GroveMiniPIRMotionSensor(pin2)
    def callback():
        return 
    pir1.on_detect = callback
    pir2.on_detect = callback
    #print("--- %s seconds ---" % (time.time() - start_time))
    while True:
        start_time = time.time()
        seconds = 4

        elapsed_time = time.time()-start_time
        if elapsed_time < seconds:
            if pir1.on_detect or pir2.on_detect:
                print('motion detected')
                return True
        else:
            print('no motion')
            return False

main()
