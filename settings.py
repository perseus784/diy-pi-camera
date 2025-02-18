import os

file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(file_path)
while (os.path.isdir(BASE_DIR)):
    if (BASE_DIR==os.path.dirname(BASE_DIR)):
        break
    else:
        BASE_DIR=os.path.dirname(BASE_DIR)
        
print(f"{BASE_DIR} is the root directory")

image_path = os.path.join("static", "images")

shutter_button_pin =  5
ISO_pins = (13, 19)
SS_pins = (6, 26)
full_res = (1920, 1080)
preview_res = (1200, 900)

sensor_defaults = {"ExposureTime": 10000, "AnalogueGain": 1.0}
ISO_RANGE = [i+1 for i in range(0,21)]
SS_RANGE = [ "1/8000", "1/4000", "1/2000", "1/1000", "1/800", "1/400", "1/200", "1/100", "1/50",
            "1/25", "1/16", "1/8", "1/4", "1/2", "1/1", "2/1", "3/1"]