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
            channel[:, :, channel_index] = frame[:, :, channel_index]
            cv2.imshow(f'{channel_initials[channel_index]}-RGB', channel)
        cv2.waitKey(0)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def LaserDection():
    # set red thresh
    lower_red = np.array([0, 0, 255])
    #lower_red = np.array([0, 0, 0])
    #156, 100, 40
    upper_red = np.array([180, 255, 255])
    #upper_red = np.array([255, 255, 255])

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame0 = cap.read()
        frame = cv2.flip(frame0, 0)
        #frame = frame[50:360, 280:380]
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        edged = cv2.Canny(mask, 30, 200)
        cv2.imshow('Canny Edges After Contouring', edged)
        print(cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE))
        #_, contours, hierarchy = cv2.findContours(
        #    edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours, hierarchy = cv2.findContours(
            edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("Number of Contours found = " + str(len(contours)))

      
        # Draw all contours
        # -1 signifies drawing all contours
        # for c in contours:
        #     M = cv2.moments(c)
        #     cX = int(M["m10"] / M["m00"])
        #     cY = int(M["m01"] / M["m00"])
        #     cv2.drawContours(frame, c, -1, (0, 255, 0), 3)
        #     cv2.circle(frame, (cX, cY), 2, (255, 255, 255), -1)
        #     cv2.putText(frame, "center", (cX - 20, cY - 20),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow('Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Works()

    LaserDection()

    #CaptureObejct = VideoCamera()
    # while(1):
    #
    #    VideoOpencv(1)

    print('succuss')
