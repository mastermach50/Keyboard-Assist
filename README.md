# Keyboard-Assist
A system tray application written in python that will assist you with your keyboard endeavors. It has features such as abbreviation, email autofill, media control, writing from clipboard ,typing current date and time etc.

---

## Requirements
   The following python modules have to be available :
 - [pystray](https://github.com/moses-palmer/pystray)
 - [keyboard](https://github.com/boppreh/keyboard)
 - PIL
 - datetime
 - pyperclip
 - os
 - json
 - subprocess

  Certain features such submenu may not be available depending on your operating system, please refer to [pystray documentation](https://pystray.readthedocs.io/en/latest/usage.html) for more info on this. There won't be any issues on Windows 10 as of my knowledge.

---

## Buttons In System Tray
<img alt="tray sample" height = 150 src="https://user-images.githubusercontent.com/64970593/134365306-15e599ed-d4e1-4efc-8699-996d51515ca9.png">


## Active
(Enabled by default)

The `Active` check allow you to activate/deactivate all the features. This includes `abbreviations`, `date and time`, `writing from clipboard`, `media controls` etc.

> Note: <br>
Although `Active` starts the `abbreviations` and `date and time`, it will not re-enable the `write from clipboard` or `media control` feature if they was enabled before. This has to be manually enabled after re-activation.

## Exit
Exit from the program.

## Write from Clipboard
The `write from clipboard` feature will enable writing from clipboard.
> The difference between pasting text and `writing from clipboard` is that in write from clipboard text is entered by sending key press events to the system, this allows the user to "paste" text into places where only typing is allowed, such as certain forms, text boxes in certain applications etc.

Once enabled all `ctrl + v` events will be suppressed, therefore no items other than text can be pasted using `ctrl + v`.

---

## Abbreviations
(Enabled when Active)

Abbreviations have to be added in the `abbr.json` file in the following format :
```json
{
    "abbrs": {
        "short": "loooooooong",
        "newshort": "newloooong"
    },
    "mails": {
        "example1000": "@gmail.com",
        "sample123": "@domain.com"
    }
}
```
If there is no `abbr.json` file in the same directory as the program file, it will create a new `abbr.json` file with the basic format.

> Abbreviations under the `abbr` section, when typed will be replaced with their given value after pressing space.

> E-mail ids under `mails` section when typed will be completed with the domain provided on pressing space.

## Date and Time
(Enabled when Active)

On typing dtt and pressing space dtt will be replaced by the current date and time.

## Media Control
(Enabled by default)

For keyboards that don't have a  media play/pause key pressing `alt + `\` will play/pause the media playing in the background (only for supported applications like chrome, vlc etc.)

> Also don't mind forking or suggesting changes, it will be a great help!
