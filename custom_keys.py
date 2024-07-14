from kmk.keys import KC
from kmk.modules.macros import Tap, Release, Press

import microcontroller


def next_boot_dfu(keyboard):
    print('setting next boot to dfu')
    microcontroller.on_next_reset(microcontroller.RunMode.UF2)


def next_boot_safe(keyboard):
    print('setting next boot to safe')
    microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)


def toggle_drive(keyboard):
    print('toggling usb drive')
    if microcontroller.nvm[0] == 0:
        microcontroller.nvm[0] = 1
    else:
        microcontroller.nvm[0] = 0


DFUMODE = KC.MACRO(next_boot_dfu)
SAFEMODE = KC.MACRO(next_boot_safe)
TOGGLEDRIVE = KC.MACRO(toggle_drive)
