import RPi.GPIO as GPIO
from gpiozero import Button

'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=playVideo)
'''

button = Button(0)

while True:
    button.when_pressed = print("button pressed")
    button.when_released = print("button released")
