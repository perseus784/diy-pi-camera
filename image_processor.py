from datetime import datetime 
from settings import image_path
import os

def save_image(camera, capture_config):
    image_file_name = os.path.join(image_path, "DSC_"+datetime.today().strftime('%Y-%m-%d-%H-%M-%S')+".jpg")
    
    image = camera.switch_mode_and_capture_request(capture_config)
    image.save('main', image_file_name)

    return image_file_name

def yourcustomfunction():
    pass