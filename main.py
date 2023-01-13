import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 14

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, True)
sleep(2)
GPIO.output(LED_PIN, False)


print('Hello, world!')
