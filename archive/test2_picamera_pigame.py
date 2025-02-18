from picamera2 import Picamera2
import pygame, os, time
from gpiozero import Button
from image_processor import process_image
from datetime import datetime
from settings import shutter_button_pin, resolution_h, resolution_w, prw_res_w, prw_res_h
import libcamera

shutter = Button(shutter_button_pin)


def save_image(camera, image):
    saved_image = process_image(camera, image)
    '''capturedFrame = pygame.image.load(saved_image).convert()
    capturedFrameRectangle = capturedFrame.get_rect()
    screen.blit(capturedFrame, capturedFrameRectangle)
    pygame.display.update()
    time.sleep(15)'''

os.environ["DISPLAY"] = ":0"

pygame.init()
res = (resolution_w, resolution_h)
preview_res = (prw_res_w, prw_res_h)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

camera = Picamera2()
camera.preview_configuration.main.size = preview_res
camera.preview_configuration.main.format = 'BGR888' 
preview_config = camera.create_preview_configuration(transform=libcamera.Transform(vflip=True), main={"size": preview_res})
camera.configure(preview_config)
camera.configure("preview")

capture_config = camera.create_still_configuration()
camera.still_configuration.main.size = camera.sensor_resolution
camera.still_configuration.buffer_count = 4

camera.start()

clock = pygame.time.Clock()
    
while True:
    array = camera.capture_array()
    img = pygame.image.frombuffer(array.data, preview_res, 'RGB')
    shutter.when_pressed = lambda: save_image(camera, capture_config)
    screen.blit(img, (0, 0))
    pygame.display.flip() # send buffer on screen
    clock.tick(25) # slow down to 25 FPS
    #time.sleep(1)

#change camera buffer size

