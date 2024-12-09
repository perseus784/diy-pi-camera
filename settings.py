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

shutter_button_pin =  26
ISO_pins = (13, 19)
SS_pins = (5, 6)
full_res = (1920, 1080)
preview_res = (1200, 900)

sensor_defaults = {"ExposureTime": 10000, "AnalogueGain": 1.0}
ISO_RANGE = [i+1 for i in range(0,15)]
SS_RANGE = []