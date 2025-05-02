from pynput.keyboard import Key, Listener

from pynput.keyboard import Listener, Key

def make_on_press(pet, pressed_keys):
    def on_press(key):
        if key not in pressed_keys:
            pressed_keys.add(key)
            pet.set_experience(pet.get_experience() + 1)
            print(pet.get_experience())
    return on_press

def make_on_release(pressed_keys):
    def on_release(key):
        pressed_keys.discard(key)  # Elimina la tecla del conjunto si está
        if key == Key.esc:
            return False
    return on_release

def count_experience(pet):
    pressed_keys = set()
    with Listener(
            on_press=make_on_press(pet, pressed_keys),
            on_release=make_on_release(pressed_keys)) as listener:
        listener.join()