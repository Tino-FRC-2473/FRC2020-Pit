#notificationnotificationclose

from PIL import Image, ImageTk
import tkinter
import PIL.Image
import tkinter as Tk, tkinter.font as tkFont
import RPi.GPIO as GPIO
from gpiozero import Button

#vars
global current_menu
current_menu = 1
print("after var")

#window setup
window = Tk.Tk()
window.title("window1")
window.config(bg='black')
screenW = window.winfo_screenwidth()
screenH = window.winfo_screenheight()
screenRatio = screenH*screenW
#window.geometry(str(screenW)+"x"+str(screenH))
#window.geometry("{0}x{1}+0+0".format(int(0.9*screenW), int(0.9*screenW*screenRatio)))
window.geometry("{0}x{1}+0+0".format(screenW, screenH))
#window.overrideredirect(1)

menu_item1 = Tk.Label(window, text = "Option 1", font = ('Helvetica', 16))
menu_item1.pack(fill = "x")
menu_item2 = Tk.Label(window, text = "Option 2", font = ('Helvetica', 16))
menu_item2.pack(fill = "x")
menu_item3 = Tk.Label(window, text = "Option 3", font = ('Helvetica', 16))
menu_item3.pack(fill = "x")
menu_item4 = Tk.Label(window, text = "Option 4", font = ('Helvetica', 16))
menu_item4.pack(fill = "x")
menu_item5 = Tk.Label(window, text = "Option 5", font = ('Helvetica', 16))
menu_item5.pack(fill = "x")

#button labels
#Previous year order: about the robot, about the team, computer vision, video game demo

label_1 = Tk.Label(window,text = "Menu",font = ('Helvetica', 16), bg = "green")
label_2 = Tk.Label(window,text = "Up",font = ('Helvetica', 16), bg = "blue")
label_3 = Tk.Label(window,text = "Down",font = ('Helvetica', 16), bg = "yellow")
label_4 = Tk.Label(window,text = "Select",font = ('Helvetica', 16), bg = "red")
label_1.pack(side = "left", fill = "both", expand = "yes")
label_2.pack(side = "left", fill = "both", expand = "yes")
label_3.pack(side = "left", fill = "both", expand = "yes")
label_4.pack(side = "left", fill = "both", expand = "yes")
print("before mainloop")


def change_bg():
    menu_item1.config(bg = "white")
    menu_item2.config(bg = "white")
    menu_item3.config(bg = "white")
    menu_item4.config(bg = "white")
    menu_item5.config(bg = "white")
    if current_menu == 1:
        menu_item1.config(bg = "gray")
    elif current_menu == 2:
        menu_item2.config(bg = "gray")
    elif current_menu == 3:
        menu_item3.config(bg = "gray")
    elif current_menu == 4:
        menu_item4.config(bg = "gray")
    elif current_menu == 5:
        menu_item5.config(bg = "gray")

'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=playVideo)
'''
print("before functions buttons")
def run_blue():
    global current_menu
    print("blue button pressed")
    if(current_menu <= 1):
        current_menu = 5
    else:
        current_menu -= 1
    change_bg()
def run_green():
    print("green button pressed")
def run_yellow():
    global current_menu
    print("yellow button pressed")
    if(current_menu >= 5):
        current_menu = 1
    else:
        current_menu += 1
    change_bg()
def run_red():
    print("red button pressed")
print("after functions buttons")
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
print("before while true")
#while True:
    #print("in while true")
    #pass
window.mainloop()
