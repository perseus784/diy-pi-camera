from picamera2 import Picamera2
import pygame, os
from gpiozero import Button
from image_processor import process_image
from datetime import datetime

shutter = Button(16)


def save_image(camera, image):
    process_image(camera, image)

os.environ["DISPLAY"] = ":0"

pygame.init()
res = (640,480)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

camera = Picamera2()
camera.preview_configuration.main.size = res
camera.preview_configuration.main.format = 'BGR888'
camera.configure("preview")
camera.start()

while True:
    array = camera.capture_array()
    img = pygame.image.frombuffer(array.data, res, 'RGB')
    shutter.when_pressed = lambda: save_image(camera, img)
    screen.blit(img, (0, 0))
    pygame.display.update()

#change camera buffer size

