import pygame, os
import cv2
from image_processor import process_image
os.environ["DISPLAY"] = ":0"

pygame.init()
res = (640,480)
screen = pygame.display.set_mode(res,pygame.FULLSCREEN) #pygame.SHOWN) #pygame.FULLSCREEN
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    processed_img = process_image(frame)
    img = pygame.image.frombuffer(processed_img, res, 'BGR')
    #button_event to trigger capture image and save process
    procesed_img = process_image(img)
    screen.blit(processed_img, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

#change camera buffer size