import time, os
from gpiozero import Button
from picamera2 import Picamera2, Preview
from libcamera import Transform
from settings import preview_res, full_res, shutter_button_pin
from datetime import datetime 
from image_processor import save_image

#IO setup
os.environ["DISPLAY"] = ":0"
shutter = Button(shutter_button_pin)


picam2 = Picamera2()
picam2.start_preview(Preview.QTGL,x=0,y=0,width=1200,height=800)

preview_config = picam2.create_preview_configuration( main={"size": preview_res}, transform=Transform(vflip=True, hflip= True))
capture_config = picam2.create_still_configuration(transform=Transform(vflip=True, hflip= True))

picam2.configure(preview_config)

picam2.start()

while True:
    if shutter.is_pressed:
        save_image(picam2, capture_config)
        #picam2.switch_mode_and_capture_file(capture_config, "images/"+"DSC_"+datetime.today().strftime('%Y-%m-%d-%H-%M-%S')+".jpg")
