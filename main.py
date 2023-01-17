import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import numpy as np
import cv2
import os


LASER_PIN = 14


def CameraModule():
    camera = PiCamera()
    camera.resolution = (600, 300)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')


def OpencvObejct():
    file_name = 'opencv.png'    

    if not os.path.exists(file_name):
        # create a PNG file
        # in current directory
        fp = open(file_name, 'x')
        fp.close()
    

    with PiCamera() as camera:
        res = [320, 480]
        camera.resolution = (res[0], res[1])
        camera.start_preview()
        camera.framerate = 24
        sleep(2)
        image = np.empty((res[0] * res[1] * 3,), dtype=np.uint8)
        camera.capture(image, 'bgr')
        image = image.reshape((res[0], res[1], 3))

        status = cv2.imwrite('opencv.png', image)

        print("Image written to file-system : ", status)


def VideoOpencv():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    
    sleep(5)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def Laser():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LASER_PIN, GPIO.OUT)
    GPIO.output(LASER_PIN, True)
    sleep(5)
    GPIO.output(LASER_PIN, False)
    


if __name__ == "__main__":
    #OpencvObejct()
    # CameraModule()
    # Laser()

    VideoOpencv()

    print('succuss')    
