import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import numpy as np
#import cv2

def CameraModule():
    camera = PiCamera()
    camera.resolution = (1920, 1080)
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

def OpencvObejct():
    with PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 24
        sleep(2)
        image = np.empty((240 * 320 * 3,), dtype=np.uint8)
        camera.capture(image, 'bgr')
        image = image.reshape((240, 320, 3))


OpencvObejct()

#CameraModule()
#LedBlink()