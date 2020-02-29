import RPi.GPIO as GPIO
from gpiozero import Button

'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=playVideo)
'''

button = Button(0)
button.when_pressed = print("button pressed")

def run():
    # if GPIO.input(0) == 1:
    #     print("Button pin 0 is off")
    #     while GPIO.input(0) == 0:
    #         print("Button pin 0 pressed")
    print("button pressed")
