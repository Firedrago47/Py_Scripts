import pynput

def key_press(key):
    print(key)

key_listener = pynput.keyboard.Listener(on_press=key_press)
with key_listener as listener:
    listener.join()