from datetime import datetime 

def process_image(camera, image):
    camera.capture_file("DSC_"+datetime.today().strftime('%Y-%m-%d-%H-%M-%S')+".jpg")
    return image