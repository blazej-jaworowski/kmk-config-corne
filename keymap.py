from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.combos import Chord, Sequence

import customkeys

keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,        KC.Y, KC.U, KC.I, KC.O, KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G,        KC.H, KC.J, KC.K, KC.L, KC.SCLN,
        KC.Z, KC.X, KC.C, KC.V, KC.B,        KC.N, KC.M, KC.COMM, KC.DOT, KC.HT(KC.SLSH, KC.RALT),
            KC.LGUI, KC.SPC, KC.LSFT,        KC.HT(KC.ENT, KC.MO(1)), KC.HT(KC.BSPC, KC.MO(2)), KC.HT(KC.ESC, KC.LCTL),
    ],
    [
        KC.PERCENT, KC.CIRCUMFLEX, KC.AMPERSAND, KC.ASTERISK, KC.TRNS,        KC.TRNS, KC.UNDERSCORE, KC.LCBR, KC.RCBR, KC.TRNS,
        KC.EXLM, KC.AT, KC.HASH, KC.DOLLAR, KC.HT(KC.MACRO('->'), KC.MO(4)),  KC.EQL, KC.MINS, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.GRV,
        KC.QUOT, KC.DQT, KC.PIPE, KC.BSLS, KC.TRNS,                           KC.TRNS, KC.PLUS, KC.LBRC, KC.RBRC, KC.TILDE,
            KC.TRNS, KC.TAB, KC.TRNS,                                         KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    [
        KC.TRNS, KC.N1, KC.N2, KC.N3, KC.TRNS,          KC.TO(3), KC.TRNS, KC.BRID, KC.BRIU, KC.TRNS,
        KC.N0, KC.N4, KC.N5, KC.N6, KC.TRNS,            KC.MPLY, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT,
        KC.TRNS, KC.N7, KC.N8, KC.N9, KC.TRNS,          KC.MUTE, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT,
        KC.TRNS, KC.TRNS, KC.TRNS,                      KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    [
        KC.F1, KC.F2, KC.F3, KC.F4, KC.TRNS,            KC.TRNS, KC.INSERT, KC.HOME, KC.PGUP, KC.PSCREEN,
        KC.F5, KC.F6, KC.F7, KC.F8, KC.TRNS,            KC.TRNS, KC.DEL, KC.END, KC.PGDOWN, KC.PAUSE,
        KC.F9, KC.F10, KC.F11, KC.F12, KC.TRNS,         KC.TRNS, customkeys.TOGGLEDRIVE, customkeys.SAFEMODE, customkeys.DFUMODE, KC.TRNS,
        KC.LCTL, KC.LALT, KC.LSFT,                      KC.LGUI, KC.RALT, KC.TO(0)
    ],
]

matrix_map = [
    -1,  0,  1,  2,  3,  4,    -1,  9,  8,  7,  6,  5,
    -1, 10, 11, 12, 13, 14,    -1, 19, 18, 17, 16, 15,
    -1, 20, 21, 22, 23, 24,    -1, 29, 28, 27, 26, 25,
    -1, -1, -1, 30, 31, 32,    -1, -1, -1, 35, 34, 33,
]


def generate_mapping():
    mapping = []

    for layer in keymap:
        mapping_layer = []
        for index in matrix_map:
            key = KC.NO if index != -1 else layer[index]
            mapping_layer.append(key)
        mapping.append(mapping_layer)

    return mapping
