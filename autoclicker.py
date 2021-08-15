import mouse
import keyboard
import time

#============================================================
'Settings'
trigger = "`"
escape = "x"
plus = "."
minus = ","
start_delay = 0.1
cps = 70
default_button = "l"
change_button_key = "/"
#============================================================

cd = 1/cps

click = None
if default_button == "l":
    click = mouse.click
elif default_button == "r":
    click = mouse.right_click

assert click

#============================================================
#cps setter
def increase(key):
    global cps
    global cd
    cps += 1
    cd = 1/cps
    print("cps is now - ", cps)

def decrease(key):
    global cps
    global cd
    if cps == 0:
        pass
    else:
        cd = 1/cps
        cps -= 1
        print("cps is now - ", cps)

keyboard.on_press_key(plus, increase, suppress = True)
keyboard.on_press_key(minus, decrease, suppress = True)

#============================================================
#button changer
def change_button(key):
    global click
    if click == mouse.click:
        click = mouse.right_click
        print("Button changed to RIGHT")
    elif click == mouse.right_click:
        click = mouse.click
        print("Button changed to LEFT")

keyboard.on_press_key(change_button_key, change_button, suppress = True)

#============================================================
#loop

while True:
    while keyboard.is_pressed(trigger):
        click()
        time.sleep(cd)
    if keyboard.is_pressed(escape):
        exit()
    else:
        time.sleep(start_delay)
