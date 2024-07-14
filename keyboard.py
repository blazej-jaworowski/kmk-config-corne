from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.stringy_keymaps import StringyKeymaps

from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.macros import Macros
from kmk.modules.capsword import CapsWord
from kmk.modules.tapdance import TapDance
from kmk.modules.split import Split, SplitSide
from kmk.scanners import DiodeOrientation

import digitalio
import board

LEFT_PINS = (
    # row pins
    (board.D6, board.D7, board.D8, board.D9),
    # col pins
    (board.D23, board.D21, board.D20, board.D22, board.D26, board.D27),
)

RIGHT_PINS = (
    # row pins
    (board.D22, board.D20, board.D23, board.D21),
    # col pins
    (board.D9, board.D8, board.D7, board.D6, board.D5, board.D4),
)


class KMKKeyboard(_KMKKeyboard):

    def __init__(self):
        self.extensions.append(MediaKeys())
        self.extensions.append(StringyKeymaps())

        self.modules.append(Layers())
        self.modules.append(HoldTap())
        self.modules.append(MouseKeys())
        self.modules.append(Macros())
        self.modules.append(CapsWord())
        self.modules.append(TapDance())

        vbus = digitalio.DigitalInOut(board.D29)
        vbus.direction = digitalio.Direction.INPUT
        side = SplitSide.RIGHT if vbus.value is False else SplitSide.LEFT

        split = Split(
            split_side=side,
            data_pin=board.D1,
            use_pio=True
        )
        self.modules.append(split)

        self.row_pins, self.col_pins = \
            RIGHT_PINS if vbus.value is False else LEFT_PINS
        self.diode_orientation = DiodeOrientation.COL2ROW

        HoldTap.tap_time = 100

        import keymap
        self.keymap = keymap.generate_mapping()
        self.debug_enabled = True
