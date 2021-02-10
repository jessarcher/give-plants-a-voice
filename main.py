import time
from gpiozero import MCP3008
from gpiozero import RGBLED
import RPi.GPIO as GPIO
import subprocess

# Config
moisture_threshold_lower = 600 # When to ask for water
moisture_threshold_upper = 700 # When to say thank you
escalation_delay = 60 * 30 # In seconds

# Pins
moisture_sensor_pin = 5
pir_pin = 21
red_pin = 13
green_pin = 19
blue_pin = 26

moisture_sensor = MCP3008(channel=0, select_pin=moisture_sensor_pin)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)
disgruntlement = 0
last_notification = 0

led = RGBLED(red=red_pin, green=green_pin, blue=blue_pin)

def moisture_below_lower_threshold():
    return moisture_sensor.value * 1023 <= moisture_threshold_lower 

def moisture_above_upper_threshold():
    return moisture_sensor.value * 1023 >= moisture_threshold_upper 

def pir_active():
    return GPIO.input(pir_pin) == 1

def ask_for_water():
    print('Disgruntled!, level: ', disgruntlement)

    if disgruntlement == 1:
        subprocess.call(["mpg123", "audio/hello-there.mp3"])

    if disgruntlement == 2:
        subprocess.call(["mpg123", "audio/awkward.mp3"])

    if disgruntlement >= 3:
        subprocess.call(["mpg123", "audio/rude.mp3"])

def say_thank_you():
    subprocess.call(["mpg123", "audio/delicious.mp3"])
    print('Thank you!')

while (1):
    print('Moisture: ', '{:.0f}'.format(moisture_sensor.value * 1023))
    print('PIR: ', GPIO.input(pir_pin))
    print('Disgruntlement: ', disgruntlement)
    print('Last Notification: ', last_notification)
    print('----------')

    if moisture_below_lower_threshold():
        led.color = (1, 0, 0) # red
    elif moisture_above_upper_threshold():
        led.color = (0, 1, 0) # green
    else:
        led.color = (1, 0.2, 0) # yellow

    if moisture_below_lower_threshold() and pir_active() and time.time() >= last_notification + escalation_delay:
        disgruntlement += 1
        ask_for_water()
        last_notification = time.time()

    if disgruntlement > 0 and moisture_above_upper_threshold() and pir_active():
        say_thank_you()
        disgruntlement = 0

    time.sleep(1)
