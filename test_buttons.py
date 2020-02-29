import RPi.GPIO as GPIO
from gpiozero import Button

'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=playVideo)
'''
def print_pressed():
    print("button pressed")

def print_released():
    print("button released")

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
button = Button(0)

button.when_pressed = print_pressed
button.when_released = print_released

while True:
    pass
