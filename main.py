from time import sleep
import numpy as np
import cv2
import os

LASER_PIN = 14

"""
import RPi.GPIO as GPIO
def Laser():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LASER_PIN, GPIO.OUT)
    GPIO.output(LASER_PIN, True)
    sleep(5)
    GPIO.output(LASER_PIN, False)
"""


def LaserDection():
    lower_red = np.array([0, 0, 255])
    upper_red = np.array([180, 255, 255])

    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame0 = cap.read()

        if !ret:
            break

        frame = cv2.flip(frame0, 0)
        #frame = frame[50:360, 280:380]
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        edged = cv2.Canny(mask, 30, 200)
        cv2.imshow('Canny Edges After Contouring', edged)
        contours, hierarchy = cv2.findContours(
            edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("Number of Contours found = " + str(len(contours)))

        cv2.imshow('Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    LaserDection()
