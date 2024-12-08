import cv2
import time, os
from picamera2 import Picamera2
from gpiozero import Button
from image_processor import save_image
from datetime import datetime
from settings import shutter_button_pin, full_res, preview_res
from libcamera import Transform

shutter = Button(shutter_button_pin)
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

while True:
    im = picam2.capture_array()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(grey,100,200)
    color_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    boolean_edges = edges==255
    im[edges==255] = [0,0,255, 255]
    
    if shutter.is_pressed:
        save_image(picam2, capture_config)
    '''faces = face_detector.detectMultiScale(grey, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))'''

    cv2.imshow("picam", im)
    cv2.waitKey(1)