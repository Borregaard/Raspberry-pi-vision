import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

camera = PiCamera()

sleep(2)
camera.capture("/Pictures/img.jpg")
print("Done.")

print('Hello, world!')

LED_PIN = 14

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

for _ in range(20):
    GPIO.output(LED_PIN, True)
    sleep(2)
    GPIO.output(LED_PIN, False)
    sleep(2)
