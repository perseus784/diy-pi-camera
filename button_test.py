from gpiozero import Button

button = Button(16)

def printx(x):
    print(x)

while True:
    button.when_pressed = lambda: printx("mymy")


