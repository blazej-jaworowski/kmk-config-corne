# flake8: noqa
# pylint: disable=line-too-long

from kmk.keys import KC
from kmk.modules.holdtap import HoldTapRepeat
from kmk.modules.macros import Tap

import custom_keys

SLSH_RALT = KC.HT(KC.SLSH, KC.RALT)
ENT_MO1 = KC.HT(KC.ENT, KC.MO(1))
BSPC_MO2 = KC.HT(KC.BSPC, KC.MO(2), repeat=HoldTapRepeat.TAP)
BSPC_MO2.tap_time = 150
ESC_LCTL = KC.HT(KC.ESC, KC.LCTL)
ARROW_MO3 = KC.HT(KC.MACRO('->'), KC.MO(3))
TG5_LSFT = KC.HT(KC.TG(5), KC.LSFT)
A_MMB = KC.HT(KC.A, KC.MB_MMB, prefer_hold=False)
D_RMB = KC.HT(KC.D, KC.MB_RMB, prefer_hold=False)
F_LMB = KC.HT(KC.F, KC.MB_LMB, prefer_hold=False)
TRNS_LCTL = KC.HT(KC.TRNS, KC.LCTL)
NUMLOCK_HOLD = KC.MACRO(
    on_press=[ Tap(KC.NUMLOCK) ],
    on_release=[ Tap(KC.NUMLOCK) ],
)

def generate_mapping():

    keymap = [
        [
            'Q',    'W',    'E',    'R',    'T',            'Y',      'U',      'I',    'O',    'P',
            A_MMB,  's',    D_RMB,    F_LMB,    'G',            'H',      'J',      'K',    'L',    ';',
            'Z',    'X',    'C',    'V',    'B',            'N',      'M',      ',',    '.',    SLSH_RALT,
                            'LGUI', 'SPC',    TG5_LSFT,         ENT_MO1,  BSPC_MO2, ESC_LCTL,
        ],
        [
            '%',    '^',    '&',    '*',    'TRNS',         'TRNS',   '_',      '{',    '}',    'TRNS',
            '!',    '@',    '#',    '$',    ARROW_MO3,      '=',      '-',      '(',    ')',    '`',
            '\'',   '"',    '|',    '\\',   'TRNS',         'TRNS',   '+',      '[',    ']',    '~',
                            'TRNS', 'TAB',  'CW',           'TRNS',   'TRNS',   'TRNS',
        ],
        [
            'TRNS', '1',    '2',    '3',    'TRNS',         KC.TG(3), 'TRNS',   'BRID', 'BRIU', 'TRNS',
            '0',    '4',    '5',    '6',    'TRNS',         'MPLY',   'LEFT',   'DOWN', 'UP',   'RIGHT',
            'TRNS', '7',    '8',    '9',    'TRNS',         'MUTE',   'MPRV',   'VOLD', 'VOLU', 'MNXT',
                            'TRNS', 'TRNS', KC.MO(4),         'TRNS',   'TRNS',   'TRNS',
        ],
        [
            'F1',   'F2',   'F3',   'F4',   'TRNS',         'TRNS',   'INSERT', 'HOME', 'PGUP', 'PSCREEN',
            'F5',   'F6',   'F7',   'F8',   'TRNS',         'TRNS',   'DEL',    'END',  'PGDOWN', 'PAUSE',
            'F9',   'F10',  'F11',  'F12',  'TRNS',         'TRNS',   custom_keys.TOGGLEDRIVE,
                                                                      custom_keys.SAFEMODE,
                                                                      custom_keys.DFUMODE,
                                                                                          'TRNS',
            'LCTL', 'LALT', 'LSFT',                         'LGUI',   'RALT',   KC.TG(3),
        ],
        [
            'TRNS',   'TRNS',   'TRNS',   'TRNS',   'TRNS',         'TRNS',   'TRNS', 'TRNS', 'TRNS', 'TRNS',
            'TRNS',   'TRNS',   'TRNS',   'TRNS',   'TRNS',         'TRNS',   'HOME',    'PGUP',  'PGDOWN', 'END',
            'TRNS',   'TRNS',  'TRNS',  'TRNS',  'TRNS',         'TRNS',   'TRNS',    'TRNS',    'TRNS',    'TRNS',
            'TRNS', 'TRNS', 'TRNS',                         'TRNS',   'TRNS',   'TRNS',
        ],
        [
            'TRNS',   'TRNS',   'TRNS',   'TRNS',   'TRNS',         'TRNS',   'TRNS', 'TRNS', 'TRNS', 'TRNS',
            'MB_MMB',   NUMLOCK_HOLD,  'MB_RMB',  'MB_LMB',   'TRNS',         'TRNS',   'TRNS',    'TRNS',  'TRNS', 'TRNS',
            'TRNS',   'TRNS',  'TRNS',  'TRNS',  'TRNS',         'TRNS',   'TRNS',    'TRNS',    'TRNS',    'TRNS',
            'TRNS', TRNS_LCTL, KC.TG(5),                         'TRNS',   'TRNS',   KC.TG(5),
        ],
    ]

    matrix_map = [
        -1,  0,  1,  2,  3,  4,    -1,  9,  8,  7,  6,  5,
        -1, 10, 11, 12, 13, 14,    -1, 19, 18, 17, 16, 15,
        -1, 20, 21, 22, 23, 24,    -1, 29, 28, 27, 26, 25,
        -1, -1, -1, 30, 31, 32,    -1, -1, -1, 35, 34, 33,
    ]

    mapping = []

    for layer in keymap:
        mapping_layer = []
        for index in matrix_map:
            key = KC.NO if index == -1 else layer[index]
            mapping_layer.append(key)
        mapping.append(mapping_layer)

    return mapping
