import cv2
import time, os
from picamera2 import Picamera2
from gpiozero import Button
from image_processor import save_image
from datetime import datetime
from settings import shutter_button_pin, ISO_pins, SS_pins
from settings import  full_res, preview_res, sensor_defaults, ISO_RANGE, SS_RANGE
from libcamera import Transform
import re
from fractions import Fraction

def parse_fraction(string):
    match = re.match(r"(\d+)/(\d+)", string)
    if match:
        return Fraction(int(match.group(1)), int(match.group(2)))
    else:
        return None

shutter = Button(shutter_button_pin)
iso_p, iso_n = Button(ISO_pins[0]), Button(ISO_pins[1])
ss_p, ss_n = Button(SS_pins[0]), Button(SS_pins[1])

os.environ["DISPLAY"] = ":0"

face_detector = cv2.CascadeClassifier("config_files/haarcascade_frontalface_default.xml")
cv2.startWindowThread()
cv2.namedWindow('picam',  cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("picam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"format": 'XRGB8888',"size": preview_res}, transform=Transform(vflip=True, hflip= True))
capture_config = picam2.create_still_configuration(transform=Transform(vflip=True, hflip= True))

picam2.configure(preview_config)

picam2.start()

sensor_config = sensor_defaults

print(picam2.camera_controls)
ISO_KEY = 0
SS_KEY = 0
SS_DISP_CALC = "auto"
ISO_DISP_CALC = "auto"

while True:
    im = picam2.capture_array()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey,100,200)
    color_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    boolean_edges = edges==255
    im[edges==255] = [0,0,255, 255]
    
    if shutter.is_pressed:
        time.sleep(0.0025)
        image_filename = save_image(picam2, capture_config)
        image_taken = cv2.imread(image_filename)
        cv2.putText(image_taken, "Storing image...", (200,200), cv2.FONT_HERSHEY_SIMPLEX, 7, (255,255,255), 4)
        cv2.imshow("picam", image_taken)
        cv2.waitKey(3000)

    elif iso_p.is_pressed:
        time.sleep(0.0025)
        if ISO_KEY == len(ISO_RANGE)-1:
            ISO_KEY = 0
        else:
            ISO_KEY += 1
        sensor_config["AnalogueGain"]= ISO_RANGE[ISO_KEY]
        picam2.set_controls(sensor_config)
        ISO_DISP_CALC = ISO_RANGE[ISO_KEY]*100

    elif iso_n.is_pressed:
        time.sleep(0.0025)
        if ISO_KEY == 0:
            ISO_KEY = len(ISO_RANGE)-1
        else:
            ISO_KEY -= 1
        sensor_config["AnalogueGain"]= ISO_RANGE[ISO_KEY]
        picam2.set_controls(sensor_config)
        ISO_DISP_CALC = ISO_RANGE[ISO_KEY]*100

    elif ss_p.is_pressed:
        time.sleep(0.0025)
        if SS_KEY == len(SS_RANGE)-1:
            SS_KEY = 0
        else:
            SS_KEY += 1
        sensor_config["ExposureTime"]= parse_fraction(SS_RANGE[SS_KEY])*1000*1000
        picam2.set_controls(sensor_config)
        SS_DISP_CALC = SS_RANGE[SS_KEY].split('/')[-1] if parse_fraction(SS_RANGE[SS_KEY])<1 else str(parse_fraction(SS_RANGE[SS_KEY]))+'"'

    elif ss_n.is_pressed:
        time.sleep(0.0025)
        if SS_KEY == 0:
            SS_KEY = len(SS_RANGE)-1
        else:
            SS_KEY -= 1
        sensor_config["ExposureTime"]= parse_fraction(SS_RANGE[SS_KEY])*1000*1000
        picam2.set_controls(sensor_config)
        SS_DISP_CALC = SS_RANGE[SS_KEY].split('/')[-1] if parse_fraction(SS_RANGE[SS_KEY])<1 else str(parse_fraction(SS_RANGE[SS_KEY]))+'"'
    
    faces = face_detector.detectMultiScale(grey, 1.05, 6, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))

    cv2.putText(im,"SS: {}        ISO: {}".format(str(SS_DISP_CALC), str(ISO_DISP_CALC)), (100,100), 0, 3, 255)
    cv2.imshow("picam", im)
    cv2.waitKey(1)