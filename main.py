import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import numpy as np
import cv2


def CameraModule():
    camera = PiCamera()
    camera.resolution = (600, 300)
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

    # create a PNG file
    # in current directory
    fp = open('opencv.png', 'x')
    fp.close()

    with PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.start_preview()
        camera.framerate = 24
        sleep(2)
        image = np.empty((240 * 320 * 3,), dtype=np.uint8)
        camera.capture(image, 'bgr')
        image = image.reshape((240, 320, 3))

        status = cv2.imwrite('opencv.png', image)

        print("Image written to file-system : ", status)


def Laser():
    LASER_PIN = 14

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LASER_PIN, GPIO.OUT)
    GPIO.output(LASER_PIN, True)
    sleep(5)
    GPIO.output(LASER_PIN, False)
    


OpencvObejct()
CameraModule()
Laser()

print('succuss')
