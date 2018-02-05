import RPi.GPIO as GPIO
import time

hum_sense_list = [7, 8]
pump_list = [15, 16]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(hum_sense_list, GPIO.IN)
    GPIO.setup(pump_list, GPIO.OUT)


def get_humidity():
    for sensor in hum_sense_list:
        state = []
        state.append(GPIO.input(sensor))
    print ("sensor " + sensor + " is " + state)
    return state

def pump_all():
    for pump in pump_list:
        GPIO.output(pump, GPIO.HIGH)
        print ("pumping " + pump)
        time.sleep(3)
        print ("stopping " + pump)
    return