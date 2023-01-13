import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera


def CameraModule():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')

def LedBlink():
    LED_PIN = 14

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

    for _ in range(20):
        GPIO.output(LED_PIN, True)
        sleep(2)
        GPIO.output(LED_PIN, False)
        sleep(2)
