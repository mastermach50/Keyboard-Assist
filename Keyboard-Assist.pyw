from pystray import Menu, MenuItem, Icon
from PIL import Image
import keyboard
import datetime
import pyperclip
import json
import os
import subprocess

# user variables=================================================================

abbrfile = "abbr.json" #your abbreviation vile
m_ctrl_shortcut = "alt + `" #media pause/play shortcut

# user variables=================================================================
# no change variables============================================================

k_active = False
wfc_active = False
m_ctrl_active = False

# no change variables============================================================
# abbrevations===================================================================


def timendate():
    # type the current time and date
    for i in range(4):
        keyboard.send("backspace")
    keyboard.write(datetime.datetime.now().strftime("%d.%m.%Y,%H-%M-%S"))


def keyboard_hooks():  # start all keyboard hooks
    # make a abbr.json file if it does not exist
    if not os.path.exists(abbrfile):
        with open(abbrfile, "w") as f:
            with open("resources\\sampleabbr.json", "r") as sample:
                f.write(sample.read())

    # load abbrevations from file
    with open(abbrfile, "r") as file:
        items = json.load(file)

    abbrs = items["abbrs"]
    for key in abbrs.keys():
        keyboard.add_abbreviation(key, abbrs[key])
    del abbrs

    # email writing
    def writemail(service):
        keyboard.send("backspace")
        keyboard.write(service)

    # load emails
    emails = items["mails"]
    for mail in emails.keys():
        keyboard.add_word_listener(mail, lambda: writemail(emails[mail]))

    # date and time
    keyboard.add_word_listener("dtt", timendate, triggers=["space"])

    del items

    # change the keyboard active variable to true
    global k_active
    k_active = True


# abbrevations===================================================================
# keyboard functions=============================================================


def change_keyboard_status(icon):
    # change the keyboard status
    global k_active, wfc_active, m_ctrl_active
    if k_active == False:
        keyboard_hooks()
    elif k_active == True:
        keyboard.unhook_all()
        k_active = False
        wfc_active = False
        m_ctrl_active = False
    icon.update_menu()


def switch_wfc(icon):
    # switches the state of the write form clipboard
    global wfc_active
    if wfc_active == True:
        keyboard.remove_hotkey("ctrl + v")
        wfc_active = False
    elif wfc_active == False:
        keyboard.add_hotkey("ctrl + v", callback=lambda: keyboard.write(pyperclip.paste()), suppress=True)
        wfc_active = True
    icon.update_menu()


def switch_media_ctrl(icon):
    # switches the state of the media control
    global m_ctrl_active
    if m_ctrl_active == True:
        keyboard.remove_hotkey(m_ctrl_shortcut)
        m_ctrl_active = False
    elif m_ctrl_active == False:
        keyboard.add_hotkey(m_ctrl_shortcut, suppress=True, callback=lambda: keyboard.send("play/pause"))
        m_ctrl_active = True
    icon.update_menu()


# keyboard functions=============================================================
# icon===========================================================================

# sets the icon using pystray
icon = Icon(
    "Keyboard-Assist",
    icon=Image.open("resources\\TrayIcon.png", "r"),
    title="Keyboard-Assist",
    menu=Menu(
        MenuItem("Keyboard-Assist", action=None, default=True, enabled=False),
        MenuItem("Active", action=change_keyboard_status, checked=lambda item: k_active),
        MenuItem("Write from Clipboard", action=switch_wfc, checked=lambda item: wfc_active),
        MenuItem("Media Control", action=switch_media_ctrl, checked=lambda item: m_ctrl_active),
        MenuItem("More", Menu(
                MenuItem("Open File Location", action=lambda: subprocess.run(["explorer.exe", os.path.split(os.path.abspath(abbrfile))[0]])))),
        MenuItem("Exit", lambda: icon.stop())
        ))

# icon===========================================================================
# start the icon and keyboard hooks without notifying
if __name__ == "__main__":
    keyboard_hooks()
    switch_media_ctrl(icon) #makes media control active
    icon.run()
