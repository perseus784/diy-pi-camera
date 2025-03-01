# DIY PI Camera
![Camera Front](data/images/camera_front.jpg?raw=true "Camera Front")
![Camera Back](data/images/camera_back.jpg?raw=true "Camera Back")
![Fusion 360](data/images/fusion-360.gif?raw=true "Fusion 360")

## Sample Images
![Sample 1](data/images/DSC_2025-03-01-13-26-09.jpg?raw=true "c1")
![sample 2](data/images/DSC_2025-03-01-13-27-13.jpg?raw=true "c2")

## Features:

### Manual Camera Settings:
ISO and Shutter Speed can be changed using the dedicated buttons to cycle through the default values.

### Gallery:
Gallery interface to view and download the images using an interactive webapp when connected to same WiFi.
![Gallery](data/images/gallery.png?raw=true "Gallery")

### Adding CV/ML Features:

Focus Peaking and Face detection using Haar cascade.
![Focus Peak](data/images/focus_peak.jpg?raw=true "Focus Peak")

add your own CV module and styling in the image_processer.py

`def yourcustom_cv_function(image):
    #add your CV processing here
    pass
`

## Run

`python3 run_picam.py`

## Accessing the images
Once connected to same WiFi, we can connect to the gallery to view and download, delete the images taken.
`python3 app.py`

## Parts and Assembly

### Parts
- Rpi 4B.
- Display module LCD.
- Battery - Pisugar S plus.
- Buttons and fasteners.

With little bit of soldering and 3D modelling, we can assemble all parts together.

### 3D files
Used Fusion-360 to give a simple design. Here: STL files.
![3D Slicer](data/images/3D_slicer.png?raw=true "3D slicer")

### Assembly and Prototyping
![Assembly1](data/images/assembly1.jpg?raw=true "Assembly1")
![Assembly2](data/images/assembly2.jpg?raw=true "Assembly2")
![Prototypes](data/images/prototypes.jpg?raw=true "Prototyping")


Please raise a PR for any file/ parts request if I missed anything, I can add it here.
