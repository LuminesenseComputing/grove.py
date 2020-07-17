import sys
# insert at 1, 0 is the script path (or '' in REPL)
# Import path to library folder
sys.path.insert(1,'../grove/')

import grove_mini_pir_motion_sensor

def main():
    # change pin number here
    pin = 12

    pir = GroveMiniPIRMotionSensor(pin)

    def callback():
        print('Motion detected.')

    pir.on_detect = callback

    while True:
        time.sleep(1)
main()
