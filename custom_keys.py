from kmk.keys import KC
from kmk.modules.macros import Tap, Release, Press


def next_boot_dfu(keyboard):
    print('setting next boot to dfu')
    import microcontroller
    microcontroller.on_next_reset(microcontroller.RunMode.UF2)

DFUMODE = KC.MACRO(next_boot_dfu)

def next_boot_safe(keyboard):
    print('setting next boot to safe')
    import microcontroller
    microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
SAFEMODE = KC.MACRO(next_boot_safe)

def toggle_drive(keyboard):
    print('toggling usb drive')
    import microcontroller
    if microcontroller.nvm[0] == 0:
        microcontroller.nvm[0] = 1
    else:
        microcontroller.nvm[0] = 0

TOGGLEDRIVE = KC.MACRO(toggle_drive)
