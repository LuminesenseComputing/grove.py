from grove_mini_pir_motion_sensor import * 

def getReadings(pin1,pin2):
 
    pir1 = GroveMiniPIRMotionSensor(pin1)
    pir2 = GroveMiniPIRMotionSensor(pin2)
    
    def callback():
        #print('Motion detected.')
        return True
    
    pir1.on_detect = callback
    '''start_time = time.time()
    seconds = 4 #can change time here

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time < seconds:
            pir1.on_detect = callback
            pir2.on_detect = callback
        if pir1.on_detect or pi2.on_detect:
            print('motion detected')
            return False
        if elapsed_time >= seconds:
            print('no motion')
            return False 
    '''
getReadings(5,16) 
