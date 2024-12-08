import os

file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(file_path)
while (os.path.isdir(BASE_DIR)):
    if (BASE_DIR==os.path.dirname(BASE_DIR)):
        break
    else:
        BASE_DIR=os.path.dirname(BASE_DIR)
        
print(f"{BASE_DIR} is the root directory")

image_path = os.path.join("images")

shutter_button_pin =  16
full_res = (1920, 1080)
preview_res = (1200, 900)