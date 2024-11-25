from datetime import datetime 
from settings import image_path
import os

def process_image(camera, image):
    image_file_name = os.path.join(image_path, "DSC_"+datetime.today().strftime('%Y-%m-%d-%H-%M-%S')+".jpg")
    camera.capture_file(image_file_name)
    return image