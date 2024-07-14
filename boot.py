import usb_cdc
import storage
import microcontroller

usb_cdc.enable(console=True, data=True)

if microcontroller.nvm[0] == 0:
    storage.disable_usb_drive()
    storage.remount("/", False)
