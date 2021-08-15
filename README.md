# Auto-Clicker

An auto clicker using the keyboard and mouse module in pyhon.

Required Python Modules :
- [keyboard](http://github.com/boppreh/keyboard)
- [mouse](http://github.com/boppreh/mouse)
- time

## Notes
- Modules have to be installed manually.
---
## Setup
- Open `Autoclicker.py` with a text editor.
- At the beginning of the file is the settings.
- Edit these to customize the settings.
---
## Settings
- trigger: the key to start clicking (release key to stop) - `str` (keyboard key)
- escape: the key to stop the program - `str` (keyboard key)
- plus: the key increase cps - `str` (keyboard key)
- minus: the key to decrease cps - `str` (keyboard key)
- start_delay: the delay before starting to click after trigger is pressed (needed for cpu usage optimization.) - `float`
- cps: clicks per second - `float`
- default_button: the default mouse button used for clicking - `str` (`r` for right and `l` for left)
- change_button: the key used to change the clicking button from left to right and vice versa - `str` (keyboard key)

### Default Settings
- trigger: `` ` ``
- escape: `x`
- plus: `.`
- minus: `,`
- start_delay: `0.1`
- cps: `70`
- default_button: `l`
- change_button: `/`
---
## Usage
### Clicking
Press the set `trigger` to start clicking at the set `cps`.
### Increasing and Decreasing CPS
Press the set `plus` or `minus` buttons to increase or decrease the cps respectively. You can also press and hold to keep increasing/decreasing the cps. The cps will be displayed in the console when changed.
### Change The Clicking Button
Press the set `change_button` key to change the mouse button used for clicking.
