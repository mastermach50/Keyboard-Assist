# Auto-Clicker-Sample

An auto clicker using the keyboard and mouse module in pyhon.

Required Python Modules :
- [keyboard](http://github.com/boppreh/keyboard)
- [mouse](http://github.com/boppreh/mouse)
- time

## Notes
- Modules have to be installed manually.

## Setup
- Open `autoclicker.py` with a text editor.
- At the beginning of the file is the settings.
- Edit these to customize the settings.

### Settings
- trigger: the key to start clicking (release key to stop) - `str`
- escape: the key to stop the program - `str`
- plus: the key increase cps - `str`
- minus: the key to decrease cps - `str`
- start_delay: the delay before starting to click after trigger is pressed. (needed for cpu usage optimization.) - `int`
- cps: clicks per second - `int`

### Default Settings
- trigger: `` ` ``
- escape: `x`
- plus: `.`
- minus: `,`
- start_delay: `0.1`
- cps: `70`
