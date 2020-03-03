import RPi.GPIO as GPIO
from gpiozero import Button
from menu import Menu 

'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=playVideo)
'''
menu = Menu()
def run_blue():
    print("blue button pressed")
    menu.up_pressed()
def run_green():
    print("green button pressed")
def run_yellow():
    print("yellow button pressed")
    menu.down_pressed()
def run_red():
    print("red button pressed")

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
blue_button = Button(0)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
green_button = Button(5)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
yellow_button = Button(6)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
red_button = Button(13)

blue_button.when_pressed = run_blue
green_button.when_pressed = run_green
yellow_button.when_pressed = run_yellow
red_button.when_pressed = run_red

while True:
    pass
