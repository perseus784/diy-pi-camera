from picamera2 import Picamera2
import pygame, os
from gpiozero import Button
from image_processor import process_image
from datetime import datetime
from settings import shutter_button_pin, resolution_h, resolution_w

shutter = Button(shutter_button_pin)


def save_image(camera, image):
    process_image(camera, image)

os.environ["DISPLAY"] = ":0"

pygame.init()
res = (resolution_w, resolution_h)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

camera = Picamera2()
camera.preview_configuration.main.size = res
camera.preview_configuration.main.format = 'BGR888'
camera.configure("preview")
camera.start()

clock = pygame.time.Clock()

while True:
    array = camera.capture_array()
    img = pygame.image.frombuffer(array.data, res, 'RGB')
    shutter.when_pressed = lambda: save_image(camera, img)
    screen.blit(img, (0, 0))
    pygame.display.flip() # send buffer on screen
    clock.tick(10) # slow down to 25 FPS

#change camera buffer size

