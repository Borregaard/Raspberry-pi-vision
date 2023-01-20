import RPi.GPIO as GPIO
from time import sleep
#from picamera import PiCamera
import numpy as np
import cv2
import os

index = 1
LASER_PIN = 14
def Laser():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LASER_PIN, GPIO.OUT)
    GPIO.output(LASER_PIN, True)
    sleep(5)
    GPIO.output(LASER_PIN, False)


class VideoCamera():
    def __init__(self):
        self.cap = cv2.VideoCapture(index, cv2.CAP_V4L)
        print(self.cap)

        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()
    
    def GetFrame(self):
        # Capture frame-by-frame
        self.ret, self.frame = self.cap.read()

        if not self.ret:
            print("Can't receive frame (stream end?). Exiting ...")
            return
        
        return self.frame
    
    def ReleaseCap(self):
        self.cap.release()


def VideoOpencv(cap2):
    cap = cv2.VideoCapture(index, cv2.CAP_V4L)
    ret, frame = cap.read()
    #frame = cap.GetFrame()

    print(frame.shape)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return

    sleep(10)
    # When everything done, release the capture
    cv2.destroyAllWindows()

def Works():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        #cv2.imshow('gray', gray)

        channel_initials = list('BGR')

        for channel_index in range(3):
            channel = np.zeros(shape=frame.shape, dtype=np.uint8)
            channel[:,:,channel_index] = frame[:,:,channel_index]
            cv2.imshow(f'{channel_initials[channel_index]}-RGB', channel)
        cv2.waitKey(0)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    Works()
    
    #CaptureObejct = VideoCamera()
    #while(1):
    #    
    #    VideoOpencv(1)

    print('succuss')
