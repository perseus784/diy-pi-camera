import cv2
import time, os
from picamera2 import Picamera2
from gpiozero import Button
from image_processor import save_image
from datetime import datetime
from settings import shutter_button_pin, ISO_pins, SS_pins
from settings import  full_res, preview_res, sensor_defaults, ISO_RANGE, SS_RANGE
from libcamera import Transform

shutter = Button(shutter_button_pin)
iso_p, iso_n = Button(ISO_pins[0]), Button(ISO_pins[1])
ss_p, ss_n = Button(SS_pins[0]), Button(SS_pins[1])

os.environ["DISPLAY"] = ":0"

#face_detector = cv2.CascadeClassifier("config_files/haarcascade_frontalface_default.xml")
cv2.startWindowThread()
cv2.namedWindow('picam',  cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("picam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"format": 'XRGB8888',"size": preview_res}, transform=Transform(vflip=True, hflip= True))
capture_config = picam2.create_still_configuration(transform=Transform(vflip=True, hflip= True))

picam2.configure(preview_config)

picam2.start()

sensor_config = sensor_defaults

print(picam2.camera_configuration())
ISO_KEY = 0
SS_KEY = 0
while True:
    im = picam2.capture_array()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(grey,100,200)
    color_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    boolean_edges = edges==255
    im[edges==255] = [0,0,255, 255]
    
    if shutter.is_pressed:
        save_image(picam2, capture_config)
    elif iso_p.is_pressed:
        print("iso_positive")
        if ISO_KEY == len(ISO_RANGE)-1:
            ISO_KEY = 0
        else:
            ISO_KEY += 1
        sensor_config["AnalogueGain"]= ISO_RANGE[ISO_KEY]
        picam2.set_controls(sensor_config)
        print(ISO_KEY, ISO_RANGE[ISO_KEY])

    elif iso_n.is_pressed:
        print("iso_n")
        if ISO_KEY == 0:
            ISO_KEY = len(ISO_RANGE)-1
        else:
            ISO_KEY -= 1
        sensor_config["AnalogueGain"]= ISO_RANGE[ISO_KEY]
        picam2.set_controls(sensor_config)
        print(ISO_KEY, ISO_RANGE[ISO_KEY])
        print(picam2.camera_properties)

    elif ss_p.is_pressed:
        print("ss_p")
    elif ss_n.is_pressed:
        print("ss_n")
    '''faces = face_detector.detectMultiScale(grey, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))'''

    cv2.putText(im,"SS: {}        ISO: {}".format(str(0), str(ISO_RANGE[ISO_KEY]*100)), (100,100), 0, 2, 255)
    cv2.imshow("picam", im)
    cv2.waitKey(1)