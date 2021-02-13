import cv2
import time


def forward(speed, delay):
    print("İleri Gidiliyor.")


def reverse(speed, delay):
    print("Geri gidiliyor.")


def turn_right(speed, delay):
    print("Sağa Dönülüyor.")


def turn_left(speed, delay):
    print("Sola dönülüyor.")


def stop():
    print("Duruluyor.")


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

left_eye, right_eye = "unreachable", "unreachable"
motor_key = "stop"

piv2cam = cv2.VideoCapture(0)

while head_width == 0:
    _, first_display = piv2cam.read()

    first_data = Oheka(display_view=first_display)
    first_grey_hue = first_data.convert_to_gray()
    first_faces = first_data.scan_cascades()

    for (x, y, w, h) in first_faces:  # birden fazla yuz varsa algilandi
        # cv2.rectangle(first_display, (x, y), (x + w, y + h), (255, 255, 255), 3)
        head_width = w
        print(head_width)

while True:
    _, display = piv2cam.read()

    gfl = Oheka(display_view=display)
    main_grey_hue = gfl.convert_to_gray()
    detected_faces = gfl.scan_cascades()
    # print(detected_faces)

    for (x, y, w, h) in detected_faces:
        roi_grey_hue = main_grey_hue[y:y + h, x:x + w]
        roi_colored = display[y:y + h, x:x + w]
        eyes = gfl.eye_cascade.detectMultiScale(roi_grey_hue, 1.3, 14)

        for (ex, ey, ew, eh) in eyes:

            if motor_key == "stop":
                if (len(eyes) == 1) and 0 < ex < 60:
                    motor_key = "turn_left"
                    turn_left(speed=50, delay=0.1)
                    left_eye = "reachable"

                elif (len(eyes) == 1) and 70 < ex < 150:
                    motor_key = "turn_right"
                    turn_right(speed=50, delay=0.1)

                elif (w - head_width) > 20:
                    motor_key = "forward"
                    forward(speed=50, delay=0.1)

                elif (head_width - w) > 20:
                    motor_key = "reverse"
                    reverse(speed=50, delay=0.1)

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

    cv2.imshow('oheka_v3.3.0', display)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
piv2cam.release()
cv2.destroyAllWindows()