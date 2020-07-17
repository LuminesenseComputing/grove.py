import sys
# insert at 1, 0 is the script path (or '' in REPL)
# Import path to library folder
sys.path.insert(1,'../grove/')

import grove_ultrasonic_ranger

def main():
    # Change pin number here
    pin = 5

    sonar = GroveUltrasonicRanger(pin)

    print('Detecting distance...')
    while True:
        print('{} cm'.format(sonar.get_distance()))
        time.sleep(1)

    return True

main()
