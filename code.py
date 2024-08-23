import keyboard
import supervisor

supervisor.runtime.autoreload = False

if __name__ == '__main__':
    kb = keyboard.KMKKeyboard()
    kb.go()
