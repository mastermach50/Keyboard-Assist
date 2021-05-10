import time
import mouse
import keyboard
import sys
import logging
#===========================================================================
'''Settings'''
tr = "`" #Trigger Key
cd = 20 #Click Delay (ms)
ek = "x" #Exit Key
lf = "<location>" #Log File Location
cps= 75 #Clicks Per Second (0 if not needed)
#===========================================================================
if cps >= 1:
    cd = 1 / cps
else:
    cd = cd/1000
    cps= 1/cd

logging.basicConfig(filename=(lf), level=logging.DEBUG, format="%(asctime)s: %(message)s")
logging.info("Started a new session")
x = 0
while True:
    if keyboard.is_pressed(tr):
        mouse.click()
        x = x + 1
        print("clicked ", x)
        time.sleep(cd)
    if keyboard.is_pressed(ek):
        cd = cd*1000
        logging.info(f"Session Ended, Clicked {x} times, Click Delay {cd} ms, CPS {cps}")
        sys.exit()
    else:
        pass
