import mouse
import keyboard
import time

#====================
'Settings'
trigger = "`"
escape = "x"
plus = "."
minus = ","
start_delay = 0.1
cps = 70
#====================

cd = 1/cps

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

while True:
    while keyboard.is_pressed(trigger):
        mouse.click()
        time.sleep(cd)
    if keyboard.is_pressed(escape):
        exit()
    else:
        time.sleep(start_delay)
