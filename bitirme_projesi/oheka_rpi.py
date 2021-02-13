# -*- coding: utf-8 -*-

import cv2
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
# GPIO.setwarning(False)

# Sol motor pinlerinin tanımlanması
SL_R_EN = 29
SL_L_EN = 31  # geri gidiş tetiklem pini
SL_RPWM = 33
SL_LPWM = 32  # 100 hızında geri gidiş

GPIO.setup(SL_R_EN, GPIO.OUT)
GPIO.setup(SL_RPWM, GPIO.OUT)
GPIO.setup(SL_L_EN, GPIO.OUT)
GPIO.setup(SL_LPWM, GPIO.OUT)
GPIO.output(SL_R_EN, True)
GPIO.output(SL_L_EN, True)
GPIO.output(SL_RPWM, 0)
GPIO.output(SL_LPWM, 0)

# Sağ motor pinlerinin tanımlanması
SG_R_EN = 21
SG_L_EN = 22
SG_LPWM = 12
SG_RPWM = 35

GPIO.setup(SG_R_EN, GPIO.OUT)
GPIO.setup(SG_RPWM, GPIO.OUT)
GPIO.setup(SG_L_EN, GPIO.OUT)
GPIO.setup(SG_LPWM, GPIO.OUT)
GPIO.output(SG_R_EN, True)
GPIO.output(SG_L_EN, True)
GPIO.output(SG_RPWM, 0)
GPIO.output(SG_LPWM, 0)


def forward():
    GPIO.output(SL_RPWM, 1)
    GPIO.output(SG_LPWM, 1)


def reverse():
    GPIO.output(SL_LPWM, 1)
    GPIO.output(SG_RPWM, 1)


def turn_right():
    GPIO.output(SL_RPWM, 1)


def turn_left():
    GPIO.output(SG_LPWM, 1)


def stop():
    GPIO.output(SL_RPWM, 0)
    GPIO.output(SG_LPWM, 0)
    GPIO.output(SL_LPWM, 0)
    GPIO.output(SG_RPWM, 0)


class Oheka:
    def __init__(self, display_view):
        self.face_cascade = cv2.CascadeClassifier("HaarCascades/haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier("HaarCascades/haarcascade_eye.xml")

        self.grey_hue, self.faces = "", ""
        self.display = display_view

    def convert_to_gray(self):
        self.grey_hue = cv2.cvtColor(self.display, cv2.COLOR_BGR2GRAY)
        return self.grey_hue

    def scan_cascades(self):
        self.faces = self.face_cascade.detectMultiScale(self.grey_hue, 1.3, 14)
        return self.faces


head_width = 0
width_variable_forward = 0
width_variable_reverse = 0

motor_key = "stop"

piv2cam = cv2.VideoCapture(0)

while head_width == 0:
    _, first_display = piv2cam.read()

    first_data = Oheka(display_view=first_display)
    first_grey_hue = first_data.convert_to_gray()
    first_faces = first_data.scan_cascades()

    for (x, y, w, h) in first_faces:  # birden fazla yuz varsa algilandi
        cv2.rectangle(first_display, (x, y), (x + w, y + h), (255, 255, 255), 3)
        head_width = w
        print(head_width)

while True:
    _, display = piv2cam.read()

    gfl = Oheka(display_view=display)
    main_grey_hue = gfl.convert_to_gray()
    detected_faces = gfl.scan_cascades()

    for (x, y, w, h) in detected_faces:
        roi_grey_hue = main_grey_hue[y:y + h, x:x + w]
        roi_colored = display[y:y + h, x:x + w]
        eyes = gfl.eye_cascade.detectMultiScale(roi_grey_hue, 1.3, 14)

        for (ex, ey, ew, eh) in eyes:

            if motor_key == "stop":
                if (len(eyes) == 1) and 0 < ex < 60:
                    motor_key = "turn_left"
                    turn_left()

                elif (len(eyes) == 1) and 70 < ex < 150:
                    motor_key = "turn_right"
                    turn_right()

                elif (w - head_width) > 20:
                    motor_key = "forward"
                    forward()

                elif (head_width - w) > 20:
                    motor_key = "reverse"
                    reverse()

            if motor_key == "forward" and (w - head_width) < 10:
                motor_key = "stop"
                stop()

            elif motor_key == "reverse" and (head_width - w) < 10:
                motor_key = "stop"
                stop()

            elif motor_key == "turn_left" and len(eyes) == 2:
                motor_key = "stop"
                stop()

            elif motor_key == "turn_right" and len(eyes) == 2:
                motor_key = "stop"
                stop()

    cv2.imshow('oheka_v3.2.8', display)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
piv2cam.release()
cv2.destroyAllWindows()