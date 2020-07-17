imprt grove_ultrasonic_ranger

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
