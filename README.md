# DIY Pi Camera

<table>
    <tr>
        <td><img src="data/images/camera_front.jpg?raw=true" alt="Camera Front" title="Camera Front" width="250" /></td>
        <td><img src="data/images/camera_back.jpg?raw=true" alt="Camera Back" title="Camera Back" width="250" /></td>
        <td><img src="data/images/fusion-360.gif?raw=true" alt="Fusion 360" title="Fusion 360" width="250" /></td>
    </tr>
</table>

## Sample Camera Images

<table>
    <tr>
        <td><img src="static/images/DSC_2025-03-01-13-26-09.jpg?raw=true" alt="c1" title="c1" width="400" /></td>
        <td><img src="static/images/DSC_2025-03-01-13-58-26.jpg?raw=true" alt="c2" title="c2" width="400" /></td>
    </tr>
    <tr>
        <td><img src="static/images/DSC_2025-03-01-14-00-04.jpg?raw=true" alt="c2" title="c2" width="400" /></td>
        <td><img src="static/images/DSC_2025-02-23-22-12-32.jpg?raw=true" alt="c2" title="c2" width="400" /></td>
    </tr>
    <tr>
        <td><img src="static/images/DSC_2025-03-01-14-02-32.jpg?raw=true" alt="c2" title="c2" width="400" /></td>
        <td><img src="static/images/DSC_2025-03-01-14-00-25.jpg?raw=true" alt="c2" title="c2" width="400" /></td>
    </tr>
</table>

## Features:

### Manual Camera Settings:
ISO and Shutter Speed can be changed using the dedicated buttons to cycle through the default values.
```
ISO Range : 100 - 2100
Shutter Speed : 1/8000 - 3 Secs
```

### Gallery:
Gallery interface to view and download the images using an interactive webapp when connected to same WiFi.
<img src="data/images/gallery.png?raw=true" alt="gallery" width="800"/>


### Adding CV/ML Features:

Focus Peaking and Face detection using Haar cascade.
<img src="data/images/focus_peak.jpg?raw=true" alt="focus_peak" width="500"/>

Add your own CV module and styling in the `image_processer.py`

```
def yourcustom_cv_function(image):
    #add your CV processing here
    pass
```

## Run

`python3 run_picam.py`

## Accessing the images
Once connected to same WiFi, we can connect to the gallery to view and download, delete the images taken.

`python3 app.py`

## Parts and Assembly

### Parts
- RPi 4B.
- Display module LCD.
- Battery - Pisugar S plus.
- Buttons and fasteners.

With little bit of soldering and 3D modelling, assembling all parts together.

Used Fusion-360 to give a simple design. Here: [STL files](https://github.com/perseus784/diy-pi-camera/tree/main/data/3D%20files).

<img src="data/images/3D_slicer.png?raw=true" alt="3D Slicer" width="800"/>

<table>
    <tr>
        <td><img src="data/images/assembly1.jpg?raw=true" alt="Assembly1" title="Assembly1" width="250" /></td>
        <td><img src="data/images/assembly2.jpg?raw=true" alt="Assembly2" title="Assembly2" width="250" /></td>
        <td><img src="data/images/prototypes.jpg?raw=true" alt="Prototyping" title="Prototyping" width="250" /></td>
    </tr>
</table>

Please raise a PR for any file/ parts request if I missed anything, I can add it here.
